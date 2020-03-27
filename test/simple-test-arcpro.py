# manual test (not a unit test)
print("="*40)
import sys
import archook

pre = []
for p in sys.path:
    pre.append(p)

r = archook.get_arcpy(pro=True)
print("ArcGIS Pro archook result: %s" % r)

post = []
for p in sys.path:
    post.append(p)

try:
    import arcpy
    print(f"Arcpy Workspace: {arcpy.env.workspace}")

except ImportError as e:
    print(f"\n{e}\n")
    print(f"\nPre sys.path: {pre}")
    print(f"\nPost sys.path: {post}")

