from pyrosim import pyrosim
import pybullet as p
import constants as c
import numpy as np

class MOTOR:
    def __init__(self, jointName, robotId):
        self.jointName = jointName
        self.robotId = robotId
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        if self.jointName == "Torso_BackLeg":
            self.amplitude = c.ROBOT_AMPLITUDE / 2
            self.frequency  = c.ROBOT_FREQUENCY / 2
            self.offset    = 0
        else:  
            self.amplitude = c.ROBOT_AMPLITUDE
            self.frequency  = c.ROBOT_FREQUENCY
            self.offset    = c.ROBOT_PHASE_SHIFT

        self.motorValues = self.amplitude * np.sin(2 * np.pi * self.frequency * np.linspace(0, 1, c.SIMULATION_STEPS) + self.offset)

    def Set_Value(self, step):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = self.robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[step],
            maxForce = c.MAX_MOTOR_FORCE
            )
    
    def Save_Values(self):
        np.save("data/" + self.jointName + "_motorValues.npy", self.motorValues)