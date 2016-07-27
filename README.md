# archook
Searches the (windows) system for arcgis and makes arcpy available to python (regardless of pythonpath/system path/registry settings)
If ArcGIS is not found, an `ImportError` is thrown.

## Example usage:
```python
try:
    import archook #The module which locates arcgis
    archook.get_arcpy()
    import arcpy
except ImportError:
    # do whatever you do if arcpy isnt there.
```

## Installation

You can pip install from GitHub:

    pip install git+ssh://git@github.com/JamesRamm/archook.git
