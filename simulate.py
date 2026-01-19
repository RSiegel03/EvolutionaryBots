import pybullet as p
import time



if __name__ == "__main__":
    physicsClient = p.connect(p.GUI)
    p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

    for i in range(1000):
        p.stepSimulation()
        time.sleep(1/60)
        print("Simulation step:", i)

    p.disconnect()
