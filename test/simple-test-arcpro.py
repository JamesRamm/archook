# manual test (not a unit test)
import sys
import os

# Add repo root to path so we can import the local archook package.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import archook
import traceback

print("=" * 40)
print(sys.version)

print("\n--- PRE sys.path:")
for x in sys.path:
    print(x)
print("---")

r = archook.get_arcpy(pro=True)
print("\n--- ArcGIS Pro archook result: %s" % r)
print("---")

print("\n--- archook version: %s" % archook.version)
print("---")


print("\n--- POST sys.path:")
for x in sys.path:
    print(x)
print("---")

print("\n--- ArcGIS-related sys.path:")
for x in sys.path:
    if "ArcGIS" in x or "arcgispro-py3" in x:
        print(x)
print("---")

print("\n--- ArcGIS-related PATH:")
for x in os.environ.get("PATH", "").split(os.pathsep):
    if "ArcGIS" in x or "arcgispro-py3" in x:
        print(x)
print("---")

try:
    import arcpy

    print(f"\n--- Arcpy Workspace: {arcpy.env.workspace}")

except ImportError as e:
    print(f"\n*** Error: {e}\n")
    print(traceback.format_exc())
