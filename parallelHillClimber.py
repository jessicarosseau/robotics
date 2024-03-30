import copy
from solution import SOLUTION
import constants as c
import random
import os


class PARALLEL_HILL_CLIMBER:
    def __init__(self):

        os.system("rm brain*.nndf")
        os.system("rm fitness*.nndf")

        self.parents = {}

        self.nextAvailableID = 0

        for i in range(c.populationSize):
            print(self.nextAvailableID)

            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve_For_One_Generation(self):

        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Print(self):
        print("\n")
        for key in self.parents.keys():
            print("Parent Fitness:", str(self.parents[key].fitness), "Child Fitness:", str(self.children[key].fitness))
        print("\n")

    def Show_Best(self):
        # self.parent.Evaluate("GUI")
        lowestFitness = {}
        minFitness = self.parents[0]
        for key in self.parents.keys():
            current = self.parents[key]
            if current.fitness < minFitness.fitness:
                minFitness = current
                print("\nUpdated minFitness with new value: " + str(minFitness.fitness))
        print("\nBest Self Identified Generating visual representation\n")
        minFitness.Start_Simulation("GUI")
        print("New value is:  " + str(minFitness.fitness))

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

        self.Show_Best()

    def Spawn(self):
        self.children = {}

        for key in self.parents.keys():
            unit = copy.deepcopy(self.parents[key])
            self.nextAvailableID += 1
            self.children[key] = unit

    def Mutate(self):
        for key in self.children.keys():
            self.children[key].Mutate()

    def Select(self):
        for unit in self.parents:
            if self.children[unit].fitness < self.parents[unit].fitness:
                self.parents[unit] = self.children[unit]

    def Evaluate(self, solutions):
        for key in solutions.keys():
            solutions[key].Start_Simulation("DIRECT")

        for key in solutions.keys():
            solutions[key].Wait_For_Simulation_To_End()