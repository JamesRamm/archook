"""
Locate ArcPy and add it to the path
Created on 13 Feb 2015
@author: Jamesramm
"""
import glob
import inspect
import os
import struct
import sys

try:
    import _winreg
except ImportError:
    import winreg as _winreg


class ArcGISBitnessError(ImportError):
    """Raised when the running Python bitness does not match ArcGIS."""



def get_python_bitness():
    """Return bit size of active python interpreter (ie. 32, 64)"""
    return struct.calcsize("P") * 8



def get_arc_bitness(pro=False):
    """Return 32 or 64 bit nature of ArGIS binaries."""
    # Pro is always 64bit
    if pro:
        return 64
    install_dir = locate_arcgis()
    if os.path.exists(os.path.join(install_dir, "bin64")):
        return 64
    elif os.path.exists(os.path.join(install_dir, "bin")):
        return 32
    return None



def verify_bit_match(pro=False):
    """Return true if python interpreter and ArcGIS bitness match each other"""
    pybits = get_python_bitness()
    arcbits = get_arc_bitness(pro)
    match = pybits == arcbits
    if not match:
        raise ArcGISBitnessError(
            "\n*** Error: python and arcgis 32/64bit mismatch: Py:{}, Arc:{}\n".format(
                pybits, arcbits
            )
        )
    return match



def verify_conda_meta_dir():
    """Issue warning if conda-meta folder does not exist

    Arcpy checks folder exists regardless of whether actually using conda.
    (https://github.com/JamesRamm/archook/issues/22#issuecomment-624262435)
    """
    cmeta = os.path.join(sys.exec_prefix, "conda-meta")
    if not os.path.exists(cmeta):
        print(
            """
Doesn't exist:
   {cmeta}

   You may need to create this directory if you get an error like:

   ImportError(\"arcpy needs to run within an active ArcGIS Conda environment\")
""".format(cmeta=cmeta)
        )
    return



def locate_arcgis(pro=False):
    """
    Find the path to the ArcGIS Desktop installation, or the ArcGIS Pro installation
    if `pro` argument is True.

    Keys to check:

    ArcGIS Pro: HKLM/SOFTWARE/ESRI/ArcGISPro 'InstallDir'

    HLKM/SOFTWARE/ESRI/ArcGIS 'RealVersion' - will give the version, then we can use
    that to go to
    HKLM/SOFTWARE/ESRI/DesktopXX.X 'InstallDir'. Where XX.X is the version

    We may need to check HKLM/SOFTWARE/Wow6432Node/ESRI instead
    """
    try:
        if pro:
            pro_key = get_pro_key()
            install_dir = _winreg.QueryValueEx(pro_key, "InstallDir")[0]
        else:
            key = _winreg.OpenKey(
                _winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Wow6432Node\ESRI\ArcGIS", 0
            )

            version = _winreg.QueryValueEx(key, "RealVersion")[0][:4]

            key_string = r"SOFTWARE\Wow6432Node\ESRI\Desktop{0}".format(version)
            desktop_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, key_string, 0)

            install_dir = _winreg.QueryValueEx(desktop_key, "InstallDir")[0]
        return install_dir
    except WindowsError:
        raise ImportError("Could not locate the ArcGIS directory on this machine")



def get_pro_paths():
    """Return 2 lists, for adding to Windows PATH and python sys.path"""
    P = locate_arcgis(pro=True)
    C = locate_pro_conda()
    python_zip = locate_pro_python_zip(C)
    PRO_WIN_PATHS = inspect.cleandoc(
        r"""
        {C}
        {C}\Library\bin
        {P}\bin
        """.format(C=C, P=P)
    )
    PRO_SYSPATHS = inspect.cleandoc(
        r"""
        {C}
        {python_zip}
        {C}\DLLs
        {C}\lib
        {C}\lib\site-packages
        {P}\bin
        {P}\Resources\ArcPy
        {P}\Resources\ArcToolbox\Scripts
        """.format(C=C, P=P, python_zip=python_zip)
    )
    winpaths = PRO_WIN_PATHS.splitlines()
    syspaths = PRO_SYSPATHS.splitlines()
    return [winpaths, syspaths]



def get_arcpy(pro=False):
    """
    Allows arcpy to imported on 'unmanaged' python installations (i.e. python installations
    arcgis is not aware of).
    Gets the location of arcpy and related libs and adds it to sys.path
    Looks for ArcGIS Pro if `pro` argument is True.
    """
    install_dir = locate_arcgis(pro)

    if pro:
        verify_bit_match(pro)
        verify_conda_meta_dir()

        winpaths, syspaths = get_pro_paths()
        for wp in winpaths:
            os.add_dll_directory(wp)
        for path in syspaths:
            sys.path.insert(0, path)

    else:
        verify_bit_match()
        arcpy = os.path.join(install_dir, "arcpy")
        if not os.path.exists(arcpy):
            raise ImportError(
                "Could not find arcpy directory in {0}".format(install_dir)
            )

        if get_arc_bitness() == 64:
            bin_dir = os.path.join(install_dir, "bin64")
        else:
            bin_dir = os.path.join(install_dir, "bin")

        dirs = ["", arcpy, bin_dir, "ArcToolbox/Scripts"]
        for p in dirs:
            sys.path.insert(0, os.path.join(install_dir, p))



def locate_pro_conda():
    """
    Returns the path to the ArcGIS Pro-managed conda environment.
    """
    try:
        pro_key = get_pro_key()
        conda_root = _winreg.QueryValueEx(pro_key, "PythonCondaRoot")[0]
        conda_env = _winreg.QueryValueEx(pro_key, "PythonCondaEnv")[0]
        conda_path = os.path.join(conda_root, "envs", conda_env)
        if not os.path.exists(conda_path):
            raise ImportError(
                "Could not find Conda environment {} in root directory {}".format(
                    conda_env, conda_root
                )
            )
        return conda_path
    except WindowsError:
        raise ImportError("Could not locate the Conda directory on this machine")





def locate_pro_python_zip(conda_path):
    """Return the Python zip file inside the ArcGIS Pro conda environment."""
    candidates = sorted(glob.glob(os.path.join(conda_path, "python*.zip")))
    if not candidates:
        raise ImportError(
            "Could not locate the Python zip file in {}".format(conda_path)
        )
    return candidates[0]


def get_pro_key():
    """
    Returns ArcGIS Pro's registry key.
    """
    pro_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\ESRI\ArcGISPro")
    return pro_key



def thankyou():
    d = {}
    d[
        "@logan-pugh"
    ] = "Python and Arc bit level must be the same\n\t (https://github.com/JamesRamm/archook/issues/22)"
    d[
        "@ChristopheD"
    ] = "Concise bitness for any python version\n\t (https://stackoverflow.com/questions/1405913/how-do-i-determine-if-my-python-shell-is-executing-in-32bit-or-64bit-mode-on-os)"
    d[
        "@jesegal"
    ] = "Use format(x=x) instead of format(x) to handle both py 2 & 3"

    print("=" * 72)
    print("Thank you for the help:\n")
    for k, v in d.items():
        print("{}:\n\t{}".format(k, v))
    print("=" * 72)
