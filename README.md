[![PyPI version](https://badge.fury.io/py/archook.svg)](https://badge.fury.io/py/archook)

# archook

`archook` searches a Windows machine for ArcGIS and updates the active Python
process so `arcpy` can be imported from a Python installation that ArcGIS did
not manage directly.

If ArcGIS is not found, `archook` raises `ImportError`.

Use `pro=True` to target ArcGIS Pro instead of ArcGIS Desktop.

## Usage

### ArcGIS Desktop

```python
try:
    import archook

    archook.get_arcpy()
    import arcpy
except ImportError:
    pass
```

### ArcGIS Pro

```python
try:
    import archook

    archook.get_arcpy(pro=True)
    import arcpy
except ImportError:
    pass
```

## Install

Install the published package with `pip`:

```powershell
pip install archook
```

Install directly from GitHub:

```powershell
pip install https://github.com/JamesRamm/archook/archive/refs/heads/master.zip
```

## Develop

Requires Python 3.10 or later.

Create the project environment and install the dev tools with `uv`:

```powershell
uv sync --group dev
```

Run the test suite:

```powershell
uv run pytest -q
```

Build source and wheel distributions:

```powershell
uv build
```

## Notes

ArcGIS Pro may require a `conda-meta` directory under the active interpreter's
`sys.prefix`. If `arcpy` reports that it must run inside an active ArcGIS conda
environment, create that directory and retry.

Archook was developed by James Ramm, currently maintained by Matt Wilkie.
