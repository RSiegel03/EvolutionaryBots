# run simulate and generate.py 
import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

# remove temp files
if os.path.exists("fitness*.txt"):
    os.system("rm fitness*.txt")
if os.path.exists("brain*.urdf"):
    os.system("rm brain*.nndf")

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
