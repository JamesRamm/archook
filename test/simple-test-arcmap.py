# manual test (not a unit test)
import archook

r = archook.get_arcpy()
print("ArcGIS Desktop archook result: %s" % r)
import arcpy
print("Arcpy Workspace: %s" % arcpy.env.workspace)
del archook
del arcpy
