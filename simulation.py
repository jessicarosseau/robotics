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
import constants as  c
import random


class SIMULATION:

    def __init__(self):
        self.world = WORLD()
        self.robot = ROBOT()

        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setGravity(0, 0, -9.8)
        self.planeId = p.loadURDF("plane.urdf")
        self.robotId = p.loadURDF("body.urdf")
        p.loadSDF("world.sdf")
        pyrosim.Prepare_To_Simulate(self.robotId)