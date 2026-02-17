import pyrosim.pyrosim as pyrosim
import numpy as np
import os
import time
import constants as c

class SOLUTION:
    def __init__(self, id):
        self.myID = id
        self.weights = np.random.rand(c.numSensorNeurons,c.numMotorNeurons) * 2 -1
        self.directOrGUI = "DIRECT" # default to DIRECT, can be set to "GUI" when creating an instance of SOLUTION

    def Set_ID(self, id):
        self.myID = id

    def Start_Simulation(self, directOrGUI = "DIRECT"):
        # simulate
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()

        # simulate
        if directOrGUI.upper() not in ["DIRECT", "GUI"]:
            raise ValueError("Invalid argument for directOrGUI. Use 'DIRECT' or 'GUI'.")
        self.directOrGUI = directOrGUI.upper()
        os.system("python3 simulate.py " + self.directOrGUI + " " + str(self.myID) + " > /dev/null 2>&1 &")

    def Wait_For_Simulation_To_End(self):
        # read fitness from file
        fitnessFile = f"fitness{self.myID}.txt"
        while not os.path.exists(fitnessFile):
            time.sleep(0.01)
        with open(fitnessFile, "r") as f:
            self.fitness = float(f.read())
            f.close()

        os.system(f"rm {fitnessFile}")  # Clean up the fitness file after reading it

    # mutate
    def mutate(self):
        randomRow = np.random.randint(0, self.weights.shape[0])
        randomCol = np.random.randint(0, self.weights.shape[1])

        self.weights[randomRow, randomCol] = np.random.rand() * 2 - 1

    # create world, body, brain
    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf") # name of file to name robot
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1], 
                                    size=[1,1,1])
        # upper legs
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", 
                           position = [0,-0.5,1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5, 0], size=[0.2,1,0.2])

        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", 
                           position = [0,0.5,1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5, 0], size=[0.2,1,0.2])

        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])

        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])

        # lower legs
        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute",
                            position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])

        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute",
                            position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])

        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute",
                            position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])

        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute",
                            position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])

        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf") # name of file to name robot

        # create sensor neurons (upper legs)
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso") # function as bias since root link and always 1
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4, linkName = "RightLeg")
        
        # create sensor neurons (lower legs)
        pyrosim.Send_Sensor_Neuron(name = 5, linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 6, linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 7, linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 8, linkName = "RightLowerLeg")

        # create motor neurons (upper legs)
        pyrosim.Send_Motor_Neuron(name = 9, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 10, jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name = 11, jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name = 12, jointName = "Torso_RightLeg")

        # create motor neurons (lower legs)
        pyrosim.Send_Motor_Neuron(name = 13, jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 14, jointName = "BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 15, jointName = "LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name = 16, jointName = "RightLeg_RightLowerLeg")

        # create synapses
        for currentRow in range(self.weights.shape[0]): # names of sensor neurons
            for currentColumn in range(self.weights.shape[1]): # names of motor neurons
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+c.numSensorNeurons, weight = self.weights[currentRow,currentColumn])
        
        # end
        pyrosim.End()



    def Create_World(self):
        pyrosim.Start_SDF("world.sdf") # name of file to name world
        pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5], 
                                    size=[1,1,1])
        
        pyrosim.End()