'''
Locate ArcPy and add it to the path
Created on 13 Feb 2015
@author: Jamesramm
'''
try:
    import _winreg
except ImportError:
    import winreg as _winreg
import os
import sys


def locate_arcgis(pro=False):
    '''
    Find the path to the ArcGIS Desktop installation, or the ArcGIS Pro installation
    if `pro` argument is True.

    Keys to check:

    ArcGIS Pro: HKLM/SOFTWARE/ESRI/ArcGISPro 'InstallDir'

    HLKM/SOFTWARE/ESRI/ArcGIS 'RealVersion' - will give the version, then we can use
    that to go to
    HKLM/SOFTWARE/ESRI/DesktopXX.X 'InstallDir'. Where XX.X is the version

    We may need to check HKLM/SOFTWARE/Wow6432Node/ESRI instead
    '''
    try:
        if pro:
            pro_key = get_pro_key()
            install_dir = _winreg.QueryValueEx(pro_key, 'InstallDir')[0]
        else:
            key = _winreg.OpenKey(
                _winreg.HKEY_LOCAL_MACHINE,
                r'SOFTWARE\Wow6432Node\ESRI\ArcGIS',
                0
            )

            version = _winreg.QueryValueEx(key, 'RealVersion')[0][:4]

            key_string = r'SOFTWARE\Wow6432Node\ESRI\Desktop{0}'.format(version)
            desktop_key = _winreg.OpenKey(
                _winreg.HKEY_LOCAL_MACHINE,
                key_string,
                0
            )

            install_dir = _winreg.QueryValueEx(desktop_key, 'InstallDir')[0]
        return install_dir
    except WindowsError:
        raise ImportError('Could not locate the ArcGIS directory on this machine')


def get_arcpy(pro=False):
    '''
    Allows arcpy to imported on 'unmanaged' python installations (i.e. python installations
    arcgis is not aware of).
    Gets the location of arcpy and related libs and adds it to sys.path
    Looks for ArcGIS Pro if `pro` argument is True.
    '''
    install_dir = locate_arcgis(pro)

    if pro:
        conda_dir = locate_conda()

        # update Windows exe path
        os.environ['PATH'] = ';'.join((
            os.path.join(install_dir, 'bin'),
            os.path.join(conda_dir, r'Library\bin'),
            os.environ['PATH']
        ))

        # Update Python's path
        dirs = ['', 'bin', 'DLLs', 'lib', 'lib/site-packages',
            'Resources/ArcPy', 'Resources/ArcToolbox/Scripts']
        for p in dirs:
            sys.path.insert(0, os.path.join(install_dir, p))

        #shouldn;t this already be in sys.path?
        #sys.path.append(os.path.join(conda_dir, r'Lib\site-packages'))

    else:
        arcpy = os.path.join(install_dir, 'arcpy')
        # Check we have the arcpy directory.
        if not os.path.exists(arcpy):
            raise ImportError('Could not find arcpy directory in {0}'.format(install_dir))

        # First check if we have a bin64 directory - this exists when arcgis is 64bit
        bin_dir = os.path.join(install_dir, 'bin64')

        # check if we are using a 64-bit version of Python
        is_64bits = sys.maxsize > 2**32

        if not os.path.exists(bin_dir) or not is_64bits:
            # Fall back to regular 'bin' dir otherwise.
            bin_dir = os.path.join(install_dir, 'bin')

        scripts = os.path.join(install_dir, 'ArcToolbox', 'Scripts')
        sys.path.extend([arcpy, bin_dir, scripts])


def locate_conda():
    '''
    Returns the path to the ArcGIS Pro-managed conda environment.
    '''
    try:
        pro_key = get_pro_key()
        conda_root = _winreg.QueryValueEx(pro_key, 'PythonCondaRoot')[0]
        conda_env = _winreg.QueryValueEx(pro_key, 'PythonCondaEnv')[0]
        conda_path = os.path.join(conda_root, 'envs', conda_env)
        if not os.path.exists(conda_path):
            raise ImportError('Could not find Conda environment {} in root directory {}'.format(conda_env, conda_root))
        return conda_path
    except WindowsError:
        raise ImportError('Could not locate the Conda directory on this machine')


def get_pro_key():
    '''
    Returns ArcGIS Pro's registry key.
    '''
    pro_key = _winreg.OpenKey(
        _winreg.HKEY_LOCAL_MACHINE,
        r'SOFTWARE\ESRI\ArcGISPro'
    )
    return pro_key
