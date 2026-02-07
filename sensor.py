from pyrosim import pyrosim
import constants as c
import numpy as np

class SENSOR:
    def __init__(self, linkName, robotId):
        self.linkName = linkName
        self.Prepare_To_Sense()
    
    def Prepare_To_Sense(self):
        self.values = np.zeros(c.SIMULATION_STEPS)
    
    def Get_Value(self, step):
        self.values[step] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        np.save("data/" + self.linkName + "_sensorValues.npy", self.values)
