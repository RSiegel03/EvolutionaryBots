import pybullet as p
import pybullet_data
import time
import numpy as np
from pyrosim import pyrosim
import random



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


    # set up positions for walking backleg
    amplitude_backleg = np.pi / 3
    frequency_backleg =  15 # Hz
    phase_shift_backleg = 0  # 90 degrees
    targetAngles_backleg = (amplitude_backleg * np.sin(2 * np.pi * frequency_backleg * np.linspace(0, 1, step_ct) + phase_shift_backleg))

    # set up positions for walking frontleg
    amplitude_frontleg = np.pi / 3
    frequency_frontleg = 15  # Hz
    phase_shift_frontleg = np.pi /2  # 180 degrees
    targetAngles_frontleg = (amplitude_frontleg * np.sin(2 * np.pi * frequency_frontleg * np.linspace(0, 1, step_ct) + phase_shift_frontleg))
    
    # simulate
    for i in range(step_ct):
        p.stepSimulation()

        time.sleep(1/100)

        # add sensor to body (touch sensor on leg for touching ground)
        backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

        # add motor to backleg
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles_backleg[i], # No movement
        maxForce = 17.5)

        # add motor to frontleg
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles_frontleg[i], # No movement
        maxForce = 17.5)

    p.disconnect()

    # save data
    # np.save("data/backLegSensorValues.npy", backLegSensorValues)
    # np.save("data/frontLegSensorValues.npy", frontLegSensorValues)
    # np.save("data/targetAngles_backleg.npy", targetAngles_backleg)
    # np.save("data/targetAngles_frontleg.npy", targetAngles_frontleg)