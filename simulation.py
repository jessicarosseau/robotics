from robot import ROBOT
from world import WORLD

import math
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os
import math
import constants as c
import random


class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT()

        # p.disconnect()
        # pyrosim.Prepare_To_Simulate(self.robotId)

    def __del__(self):

        p.disconnect()

    def Run(self):
        for i in range(c.num_steps):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Sense(i)
            time.sleep(1 / 120)
