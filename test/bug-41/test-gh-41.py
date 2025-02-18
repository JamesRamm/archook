# /// script
# requires-python = "~=3.11"
# dependencies = [
#     "archook @ https://github.com/JamesRamm/archook.git",
#     "arcgis-mapping"
# ]
# ///

"""Test script for issue #41: ArcPy DLL loading failure with Pro=True.

This script attempts to load arcpy using archook with pro=True setting,
which currently results in a DLL initialization error.

Original recipe:

> uv venv --python 3.11
> uv pip install https://github.com/JamesRamm/archook.git
> mkdir .venv\conda-meta
> uv run python
    >>> import archook
    >>> archook.get_arcpy(pro=True)
    >>> import arcpy
    ImportError: DLL load failed while importing _arcgisscripting: A dynamic link library (DLL) initialization routine failed.
"""

import os
import archook

def main():
    # # Set CONDA_META_DIR to a local directory
    # local_conda_meta = os.path.join(os.path.dirname(__file__), 'conda-meta')
    # os.makedirs(local_conda_meta, exist_ok=True)
    # os.environ['CONDA_META_DIR'] = local_conda_meta
    # print(f"Set CONDA_META_DIR to: {local_conda_meta}")
    
    print("Attempting to get arcpy with pro=True...")
    archook.get_arcpy(pro=True)
    
    print("Attempting to import arcpy...")
    try:
        import arcpy
        print("Successfully imported arcpy")
    except ImportError as e:
        print(f"Failed to import arcpy: {e}")
        raise

if __name__ == "__main__":
    main()
