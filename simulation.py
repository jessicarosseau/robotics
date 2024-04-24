from world import WORLD
from robot import ROBOT
from sensor import SENSOR
from motor import MOTOR

import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c

class SIMULATION:

    def __init__(self, direction, solutionID,frequency, duration):
        self.frequency = frequency
        self.duration = duration
        self.directOrGUI = direction
        if direction == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif direction == "GUI":
            self.physicsClient = p.connect(p.GUI)
        else:
            print("Invalid direction")

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)

    def Run(self):
        #c.runs
        for t in range(self.duration):
            # if self.directOrGUI == "GUI":
            #     time.sleep(1/240)
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
        #input("Press Enter to exit...")


    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()

