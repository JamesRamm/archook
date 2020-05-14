# manual test (not a unit test)
import sys
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

try:
    import arcpy
    print(f"\n--- Arcpy Workspace: {arcpy.env.workspace}")

except ImportError as e:
    print(f"\n*** Error: {e}\n")
    print(traceback.format_exc())
