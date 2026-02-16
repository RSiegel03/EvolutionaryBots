import pyrosim.pyrosim as pyrosim
import numpy as np
import os
import time

class SOLUTION:
    def __init__(self, id):
        self.myID = id
        self.weights = np.random.rand(3,2) * 2 -1
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
        os.system("python3 simulate.py " + self.directOrGUI + " " + str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self):
        # read fitness from file
        fitnessFile = f"fitness{self.myID}.txt"
        while not os.path.exists(fitnessFile):
            time.sleep(0.01)
        with open(fitnessFile, "r") as f:
            self.fitness = float(f.read())
            f.close()

        # os.system(f"rm {fitnessFile}")  # Clean up the fitness file after reading it

    # mutate
    def mutate(self):
        randomRow = np.random.randint(0, self.weights.shape[0])
        randomCol = np.random.randint(0, self.weights.shape[1])

        self.weights[randomRow, randomCol] = np.random.rand() * 2 - 1

    # create world, body, brain
    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf") # name of file to name robot
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], 
                                    size=[1,1,1])
        pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0, -0.5], 
                                    size=[1,1,1])
        pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0, -0.5], 
                                    size=[1,1,1])
        

        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf") # name of file to name robot

        # create sensor neurons
        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")

        # create motor neurons
        pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_FrontLeg")

        # create synapses
        for currentRow in range(self.weights.shape[0]): # names of sensor neurons
            for currentColumn in range(self.weights.shape[1]): # names of motor neurons
                pyrosim.Send_Synapse(sourceNeuronName = currentRow, targetNeuronName = currentColumn+3, weight = self.weights[currentRow,currentColumn])
        
        # end
        pyrosim.End()



    def Create_World(self):
        pyrosim.Start_SDF("world.sdf") # name of file to name world
        pyrosim.Send_Cube(name="Box", pos=[-3,3,0.5], 
                                    size=[1,1,1])
        
        pyrosim.End()