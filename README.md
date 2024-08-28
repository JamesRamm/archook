[![PyPI version](https://badge.fury.io/py/archook.svg)](https://badge.fury.io/py/archook)

# archook
Searches the (windows) system for arcgis and makes arcpy available to python (regardless of pythonpath/system path/registry settings). It's typically used when using a python distribution that's wasn't installed by ArcGIS. Ones downloaded direct from Python.org or a conda environment for two examples.

If ArcGIS is not found, an `ImportError` is thrown.

Use `pro=True` to target ArcGIS Pro instead of ArcGIS Desktop.

## Example usage

### ArcGIS Desktop
```python
try:
    import archook #The module which locates arcgis
    archook.get_arcpy()
    import arcpy
except ImportError:
    # do whatever you do if arcpy isnt there.
```
### ArcGIS Pro
```python
try:
    import archook #The module which locates arcgis
    archook.get_arcpy(pro=True)
    import arcpy
except ImportError:
    # do whatever you do if arcpy isnt there.
```

**Note:** You may need to create a `conda-meta` directory in your Python interpreter's directory (referred to by `sys.prefix`) if you get an error like the following:

```
ImportError("arcpy needs to run within an active ArcGIS Conda environment")
```

## Installation

Regular install with pip:

    # (Preferred) install from GitHub _master_ branch
    pip install https://github.com/JamesRamm/archook/archive/master.zip

    # install latest pypi release package (lags behind)
    pip install archook 


Install in developer mode using Git:

    git clone https://github.com/JamesRamm/archook.git
    pip install --editable .\archook
    
Install in developer mode manually:

- Fetch https://github.com/JamesRamm/archook/archive/master.zip
- unzip `%userprofile%\downloads\archook-master.zip`
- run `pip install --editable path\to\archook-master`


## Exploration

Info item: as of ArcGIS Pro 2.7 arcpy is installable with Anaconda. Presumably this means you don't have to have Pro on a given machine to install and use it. (You'll still need to be able to acquire and verify a valid license of course.)

> At ArcGIS Pro 2.7, ArcPy can also be added to an existing Python environment, as long as its package versions are not in conflict. To add ArcPy, use conda to install ArcPy from the Esri channel on Anaconda Cloud. From the Python Command Prompt, run the following command:
>   `conda install arcpy -c esri`
>
https://pro.arcgis.com/en/pro-app/latest/arcpy/get-started/installing-arcpy.htm
