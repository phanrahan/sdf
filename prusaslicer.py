import subprocess

prusa='/Applications/PrusaSlicer.app/Contents/MacOS/PrusaSlicer'

def run(stl, gcode, config):
    cmd = [prusa, "--center", "125,105", "--export-gcode", "--loglevel", "0"] + \
          ["--load", config] + \
          ["--output", gcode] + \
          [stl] 
    print(cmd)
    subprocess.run(cmd)


