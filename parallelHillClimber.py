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
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    
    def Evolve(self):
        # generate initial population and evaluate fitness
        self.Evaluate(self.parents)
        
        # run generations
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for parent_idx in self.parents:
            self.children[parent_idx] = copy.deepcopy(self.parents[parent_idx])
            self.children[parent_idx].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        

    def Mutate(self):
        for child_idx in self.children:
            self.children[child_idx].mutate()
        
    def Print(self):
        for parent_idx in self.parents:
            print(f"Parent {parent_idx:>2d} fitness: {self.parents[parent_idx].fitness:>12.6f}  -- Child {parent_idx:>2d} fitness: {self.children[parent_idx].fitness:>12.6f}")
        print() 

    def Select(self):
        for parent_idx in self.parents:
            if self.children[parent_idx].fitness < self.parents[parent_idx].fitness:
                self.parents[parent_idx] = copy.deepcopy(self.children[parent_idx])

    def Evaluate(self, solutions):
        for sol_idx in solutions:
            solutions[sol_idx].Start_Simulation()
        
        for sol_idx in solutions:
            solutions[sol_idx].Wait_For_Simulation_To_End()
        

    def Show_Best(self):
        best_parent_idx = min(self.parents, key=lambda idx: self.parents[idx].fitness)
        self.parents[best_parent_idx].Start_Simulation("gui")
        
        os.system("rm fitness*.txt")  # Clean up any remaining fitness files after showing the best solution

    
