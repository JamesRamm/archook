# manual test (not a unit test)
import archook

r = archook.get_arcpy()
print("ArcGIS Desktop archook result: %s" % r)

r = archook.get_arcpy(pro=True)
print("ArcGIS Pro archook result: %s" % r)
