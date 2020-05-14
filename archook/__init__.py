from .archook import locate_arcgis, get_arcpy

__all__ = ["locate_arcgis", "get_arcpy"]

from setuptools_scm import get_version
version = get_version(root='..', relative_to=__file__)