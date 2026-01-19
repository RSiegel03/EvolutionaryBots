import pyrosim.pyrosim as pyrosim

if __name__ == "__main__":
    pyrosim.Start_SDF("boxes.sdf") # name of file to name world

    length, width, height = 1, 1, 1
    x, y, z = 0, 0, 0.5
    pyrosim.Send_Cube(name="Box", pos=[x,y,z], 
                      size=[length,width,height]) # (x,y,z), (l,w,h)
    length, width, height = 1, 1, 1
    x, y, z = 1, 0, 1.5
    pyrosim.Send_Cube(name="Box2", pos=[x,y,z], 
                      size=[length,width,height])
    pyrosim.End()