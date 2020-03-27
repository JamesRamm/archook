# manual test (not a unit test)
import archook

r = archook.get_arcpy(pro=True)
print("ArcGIS Pro archook result: %s" % r)
import arcpy
print(f"Arcpy Workspace: {arcpy.env.workspace}")
