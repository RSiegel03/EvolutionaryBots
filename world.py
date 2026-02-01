import pybullet as p
import pybullet_data
import constants as c
from pyrosim import pyrosim

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")