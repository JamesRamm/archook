from .archook import locate_arcgis, get_arcpy
from os import path

__all__ = ["locate_arcgis", "get_arcpy"]

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "VERSION")) as f:
    version = f.read().strip()
