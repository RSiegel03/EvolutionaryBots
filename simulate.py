from simulation import SIMULATION
import sys
import constants as c

if __name__ == "__main__":
    directOrGUI = sys.argv[1]

    simulation = SIMULATION(directOrGUI)

    if directOrGUI.upper() == "GUI":
        timestep = c.TIME_STEP
    else:
        timestep = 0
    simulation.Run(timeStep=timestep)