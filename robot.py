import time
import pybullet as p
import pybullet_data
import constants as c
from pyrosim import pyrosim
from sensor import SENSOR
from motor import MOTOR
import numpy as np
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robotId  = p.loadURDF("body.urdf")

        self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
        
        os.system(f"rm brain{solutionID}.nndf")  # Clean up the brain file after loading it

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

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(desiredAngle)
   

    def Save_Values(self):
        for linkName in self.sensors:
            self.sensors[linkName].Save_Values()


    def Think(self):
        self.nn.Update()
        # self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0] 
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        # store fitness in file
        with open(f"tmp{self.solutionID}.txt", "w") as f:
            f.write(str(xCoordinateOfLinkZero))
        
        os.system(f"mv tmp{self.solutionID}.txt fitness{self.solutionID}.txt")  # Rename the temporary file to the final fitness file