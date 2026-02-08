from simulation import SIMULATION
import sys
import constants as c

if __name__ == "__main__":
    directOrGUI = sys.argv[1]

    simulation = SIMULATION(directOrGUI)

    simulation.Run()