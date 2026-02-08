from pyrosim import pyrosim
from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
from pyrosim import pyrosim
import time
import numpy as np
from solution import SOLUTION
import copy

class HILL_CLIMBER:
    def __init__(self):
        self.parent = SOLUTION()
        self.parent.Evaluate("gui")
    
    def Evolve(self):
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        
        self.Show_Best()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.mutate()
        
    def Print(self):
        print("\n\nParent fitness: " + str(self.parent.fitness))
        print("Child fitness: " + str(self.child.fitness)+"\n")

    def Select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = copy.deepcopy(self.child)

    def Show_Best(self):
        self.parent.Evaluate("gui")

    
