'''
Locate ArcPy and add it to the path
Created on 13 Feb 2015
@author: Jamesramm
'''
import _winreg
import sys
from os import path
def locate_arcgis():
  '''
  Find the path to the ArcGIS Desktop installation.

  Keys to check:

  HLKM/SOFTWARE/ESRI/ArcGIS 'RealVersion' - will give the version, then we can use
  that to go to
  HKLM/SOFTWARE/ESRI/DesktopXX.X 'InstallDir'. Where XX.X is the version

  We may need to check HKLM/SOFTWARE/Wow6432Node/ESRI instead
  '''
  try:
    key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
                          'SOFTWARE\\Wow6432Node\\ESRI\\ArcGIS', 0)

    version = _winreg.QueryValueEx(key, "RealVersion")[0][:4]

    key_string = "SOFTWARE\\Wow6432Node\\ESRI\\Desktop{0}".format(version)
    desktop_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
                                  key_string, 0)

    install_dir = _winreg.QueryValueEx(desktop_key, "InstallDir")[0]
    return install_dir
  except WindowsError:
    raise ImportError("Could not locate the ArcGIS directory on this machine")

def get_arcpy():  
  '''
  Allows arcpy to imported on 'unmanaged' python installations (i.e. python installations
  arcgis is not aware of).
  Gets the location of arcpy and related libs and adds it to sys.path
  '''
  install_dir = locate_arcgis()  
  arcpy = path.join(install_dir, "arcpy")
  # Check we have the arcpy directory.
  if not path.exists(arcpy):
    raise ImportError("Could not find arcpy directory in {0}".format(install_dir))

  # First check if we have a bin64 directory - this exists when arcgis is 64bit
  bin_dir = path.join(install_dir, "bin64")
  
  # check if we are using a 64-bit version of Python
  is_64bits = sys.maxsize > 2**32
  
  if not path.exists(bin_dir) or is_64bits == False:
    # Fall back to regular 'bin' dir otherwise.
    bin_dir = path.join(install_dir, "bin")

  scripts = path.join(install_dir, "ArcToolbox", "Scripts")  
  sys.path.extend([arcpy, bin_dir, scripts])
