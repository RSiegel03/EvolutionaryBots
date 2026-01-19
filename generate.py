import pyrosim.pyrosim as pyrosim

if __name__ == "__main__":
    pyrosim.Start_SDF("boxes.sdf") # name of file to name world

    box_ct = 10
    for i in range(box_ct):
        # update for next box
        length, width, height = 0.9**(i), 0.9**(i), 0.9**(i)
        x, y, z = 0, 0, 0.5 + 1*i

        pyrosim.Send_Cube(name="Box" + str(i), pos=[x,y,z], 
                          size=[length,width,height])
        
        

    pyrosim.End()