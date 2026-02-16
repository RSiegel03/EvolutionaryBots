from simulation import SIMULATION
import sys
import constants as c

if __name__ == "__main__":
    directOrGUI = sys.argv[1] if len(sys.argv) > 1 else "DIRECT"  # Default to "DIRECT" if no argument is provided
    solutionID = sys.argv[2] if len(sys.argv) > 2 else "0"  # Default to "0" if no ID is provided
    simulation = SIMULATION(directOrGUI, solutionID)

    if directOrGUI.upper() == "GUI":
        timestep = c.TIME_STEP
    else:
        timestep = 0
    simulation.Run(timeStep=timestep)