import sys
import glob
import prusaslicer

config_base = 'config'
filament="pla"
model="mk4"
config = ".".join([config_base, filament, model, "ini"])

gcode_suffix = "bgcode" if model == 'mk4' else "gcode"

for file in glob.glob("*.stl"):
    base = file.removesuffix(".stl")
    stl = base + ".stl"
    gcode = ".".join([base, filament, model, gcode_suffix])
    print(file,stl,gcode,config)
    prusaslicer.run(stl, gcode, config)

sys.exit(1)

# In prusaslicer File -> Gcode Preview ...

