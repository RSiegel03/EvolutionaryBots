import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf") # name of file to name world

pyrosim.Send_Cube(name="Box", pos=[0,0,0.5], size=[1,1,1]) # (x,y,z), (l,w,h)

pyrosim.End()