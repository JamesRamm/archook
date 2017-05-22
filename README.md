[![PyPI version](https://badge.fury.io/py/archook.svg)](https://badge.fury.io/py/archook)
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

Install with pip:

    pip install archook
