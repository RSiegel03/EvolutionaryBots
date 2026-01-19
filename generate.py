import pyrosim.pyrosim as pyrosim

if __name__ == "__main__":
    pyrosim.Start_SDF("box.sdf") # name of file to name world

    length, width, height = 1, 2, 3
    x, y, z = 0, 0, 1.5
    pyrosim.Send_Cube(name="Box", pos=[x,y,z], 
                      size=[length,width,height]) # (x,y,z), (l,w,h)

    pyrosim.End()