# IMPORT NUMPY FOR MATHEMATICAL CONSTANTS
import numpy as np

# variables/constants for simulation
# WORLD CONSTANTS
TIME_STEP = 1/250  # seconds
GRAVITYZ = -9.8     # m/s^2
SIMULATION_STEPS = 1000  # number of simulation steps


# ROBOT CONSTANTS
MAX_MOTOR_FORCE = 17.5  # Newtons
ROBOT_AMPLITUDE = np.pi / 3  # radians
ROBOT_FREQUENCY = 10  # Hz
ROBOT_PHASE_SHIFT = 0  # radians

# HILL CLIMBER CONSTANTS
numberOfGenerations = 25
populationSize = 2
