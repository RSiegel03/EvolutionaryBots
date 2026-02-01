import pybullet as p
import pybullet_data
import constants as c
from pyrosim import pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy as np

class ROBOT:
    def __init__(self):
        self.robotId  = p.loadURDF("body.urdf")


    def Prepare_To_Sense(self):
        self.sensors = dict()

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName, self.robotId)

    def Sense(self, step):
        for linkName in self.sensors:
            self.sensors[linkName].Get_Value(step)

    def Prepare_To_Act(self):
        self.motors = dict()

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName, self.robotId)

    def Act(self, step):
        for jointName in self.motors:
            self.motors[jointName].Set_Value(step)

    def Save_Values(self):
        for linkName in self.sensors:
            self.sensors[linkName].Save_Values()

        for jointName in self.motors:
            self.motors[jointName].Save_Values()