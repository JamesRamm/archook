[![PyPI version](https://badge.fury.io/py/archook.svg)](https://badge.fury.io/py/archook)

# archook
Searches the (windows) system for arcgis and makes arcpy available to python (regardless of pythonpath/system path/registry settings)
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

Install with pip:

    pip install archook
