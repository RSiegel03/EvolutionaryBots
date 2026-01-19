import pybullet as p
import pybullet_data
import time



if __name__ == "__main__":
    physicsClient = p.connect(p.GUI)    
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    # p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

    
    p.setGravity(0,0,-9.8)
    planeId = p.loadURDF("plane.urdf")
    p.loadSDF("boxes.sdf")
    


    for i in range(1000):
        p.stepSimulation()
        time.sleep(1/60)
        print("Simulation step:", i)

    p.disconnect()
