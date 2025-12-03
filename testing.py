import os
p = "/private/var/folders/q8/nf645rpd7xd2_wslc8zd02zw0000gn/T/Slicer-maarten/__SlicerTemp__2025-12-01_10+43+35.926/output-segmentation.nrrd"
print("exists:", os.path.exists(p))
if os.path.exists(p):
    print("size (bytes):", os.path.getsize(p))
