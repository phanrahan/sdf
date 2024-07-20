import sys
import glob
import prusaslicer

filament="pla"
model="mk4"
config = ".".join(["config", filament, model, "ini"])

gcode_suffix = "bgcode" if model == 'mk4' else "gcode"

for base in ["tet", "oct", "ico"]:
    stl = base + ".stl"
    gcode = ".".join([base, filament, model, gcode_suffix])
    print(stl,gcode,config)
    prusaslicer.run(stl, gcode, config)

sys.exit(1)

# In prusaslicer File -> Gcode Preview ...

