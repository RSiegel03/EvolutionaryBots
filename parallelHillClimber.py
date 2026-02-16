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

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        
        # self.parent = SOLUTION()
        # self.parent.Evaluate("gui")
    
    def Evolve(self):
        for parent_idx in self.parents:
            self.parents[parent_idx].Start_Simulation("gui")
        
        for parent_idx in self.parents:
            self.parents[parent_idx].Wait_For_Simulation_To_End()
            print(f"Parent {parent_idx} fitness: {self.parents[parent_idx].fitness}")
        
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1

    def Mutate(self):
        self.child.mutate()
        
    def Print(self):
        print("\n\nParent fitness: " + str(self.parent.fitness))
        print("Child fitness: " + str(self.child.fitness)+"\n")

    def Select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = copy.deepcopy(self.child)

    def Show_Best(self):
        pass
        # self.parent.Evaluate("gui")

    
