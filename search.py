# run simulate and generate.py 
import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()

# for _ in range(2):
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")