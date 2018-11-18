[![PyPI version](https://badge.fury.io/py/archook.svg)](https://badge.fury.io/py/archook)

<div class="alert tip">
## Call For Maintainers
I no longer work with ArcGIS so debugging issues has become impossible for me.
I'm looking for maintainer(s) to take over the project. It is a super simple project!
</div>

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
