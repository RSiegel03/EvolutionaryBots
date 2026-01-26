import pybullet as p
import pybullet_data
import time
import numpy as np
from pyrosim import pyrosim



if __name__ == "__main__":
    physicsClient = p.connect(p.GUI)    
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    # p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

    # init environment
    p.setGravity(0,0,-9.8)
    planeId = p.loadURDF("plane.urdf")
    robotId = p.loadURDF("body.urdf")
    pyrosim.Prepare_To_Simulate(robotId) # do this for any robot you load
    p.loadSDF("world.sdf")
    
    #store sensor values 
    step_ct = 1000
    backLegSensorValues = np.zeros(step_ct)
    frontLegSensorValues = np.zeros(step_ct)


    # simulate
    for i in range(step_ct):
        p.stepSimulation()
        time.sleep(1/60)

        # add sensor to body (touch sensor on leg for touching ground)
        backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")


    p.disconnect()

    # save data
    np.save("data/backLegSensorValues.npy", backLegSensorValues)
    np.save("data/frontLegSensorValues.npy", frontLegSensorValues)