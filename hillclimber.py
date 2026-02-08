from pyrosim import pyrosim
from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
from pyrosim import pyrosim
import time
import numpy as np
from solution import SOLUTION

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()
    
