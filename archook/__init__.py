from .archook import locate_arcgis, get_arcpy

__all__ = ["locate_arcgis", "get_arcpy"]

def get_version():
    try:
        from setuptools_scm import get_version
        return get_version(root='..', relative_to=__file__, fallback_version = '1.3')
    except (ImportError, LookupError):
        from pkg_resources import get_distribution
        return get_distribution(__package__).version

version = get_version()