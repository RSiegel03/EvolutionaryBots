from pyrosim import pyrosim
from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
from pyrosim import pyrosim
import time
import numpy as np

class SIMULATION:
    def __init__(self, directOrGUI):
        # Initialize PyBullet physics client
        self.directOrGUI = directOrGUI.upper()
        if self.directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)
        else:
            self.physicsClient = p.connect(p.DIRECT)  # Use DIRECT for non-graphical version
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # init environment
        p.setGravity(0, 0, c.GRAVITYZ)

        #load world and robot
        self.world = WORLD()
        self.robot = ROBOT()

        # Prepare Pyrosim for simulation
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()

    def Run(self):
        # simulate
        for i in range(c.SIMULATION_STEPS):
            p.stepSimulation()

            if self.directOrGUI == "GUI":
                time.sleep(c.TIME_STEP)

            # sense and act
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()

            #evalulat
            self.Get_Fitness()



    def __del__(self):
        p.disconnect()
        self.robot.Save_Values()

    def Get_Fitness(self):
        self.robot.Get_Fitness()

