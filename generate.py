import pyrosim.pyrosim as pyrosim

if __name__ == "__main__":
    pyrosim.Start_SDF("boxes.sdf") # name of file to name world

    box_ct = 10
    length, width, height = 1, 1, 1
    x, y, z = 0, 0, 0.5
    for i in range(box_ct):
        pyrosim.Send_Cube(name="Box" + str(i), pos=[x,y,z], 
                          size=[length,width,height])
        
        # update for next box
        length, width, height = 0.9**(i+1), 0.9**(i+1), 0.9**(i+1)
        z += 1

    pyrosim.End()