# manual test (not a unit test)
print("="*40)
import sys
import archook
import traceback

print(sys.version)

print("\n--- PRE sys.path:")
for x in sys.path:
    print(x)

r = archook.get_arcpy()
print("\n--- ArcGIS Desktop archook result: %s" % r)

print("\n--- POST sys.path:")
for x in sys.path:
    print(x)

try:
    import arcpy
    print("\n--- Arcpy Workspace: %s" % arcpy.env.workspace)

except ImportError as e:
    print("\n*** Error: %s\n" % e)
    print(traceback.format_exc())
