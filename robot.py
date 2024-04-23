# import pybullet as p
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# from sensor import SENSOR
# from motor import MOTOR
# import constants as c
# import numpy
# from pyrosim.neuralNetwork import NEURAL_NETWORK
# import os
#
#
# class ROBOT:
#
#     def __init__(self, SolutionID):
#         self.robotId = p.loadURDF("robot.urdf")
#         pyrosim.Prepare_To_Simulate(self.robotId)
#         ROBOT.Prepare_To_Sense(self)
#         ROBOT.Prepare_To_Act(self)
#         self.ID = SolutionID
#
#         filename = "brain" + str(SolutionID)+ ".nndf"
#         filepath = os.path.join("/Users/jessica/Desktop/robotics2", filename)
#
#         try:
#             self.nn = NEURAL_NETWORK(filepath)
#         except FileNotFoundError:
#             print(f"File not found: {filepath}")
#             raise
#         except Exception as e:
#             print(f"An error occurred while loading the neural network from {filepath}: {e}")
#             raise
#
#         # Optionally remove the file if it's no longer needed
#         try:
#             os.remove(filepath)
#             print(f"Successfully removed {filepath}")
#         except Exception as e:
#             print(f"Failed to remove {filepath}: {e}")
#
#         #self.nn = NEURAL_NETWORK("brain" + str(SolutionID) + ".nndf")
#         # filename = "brain" + str(SolutionID) + ".nndf"
#         # filepath = os.path.join("/Users/jessica/Desktop/robotics2", filename)
#         # self.nn = NEURAL_NETWORK(filepath)
#         # os.system("rm brain" + str(SolutionID) + ".nndf")
#
#
#     def Prepare_To_Sense(self):
#         self.sensors = {}
#         for linkName in pyrosim.linkNamesToIndices:
#             self.sensors[linkName] = SENSOR(linkName)
#
#     def Sense(self, t):
#         for i in self.sensors:
#             self.sensors[i].Get_Value(t)
#
#
#     def Prepare_To_Act(self):
#         self.motors = {}
#         for jointName in pyrosim.jointNamesToIndices:
#             self.motors[jointName] = MOTOR(jointName)
#
#     def Act(self, t):
#         for neuronName in self.nn.Get_Neuron_Names():
#             if (self.nn.Is_Motor_Neuron(neuronName)):
#                 jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
#                 desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
#
#                 self.motors[jointName].Set_Value(self.robotId, desiredAngle)
#
#     def Think(self):
#         self.nn.Update()
#         #self.nn.Print()
#
#     def Get_Fitness(self):
#         self.stateOfLinkZero = p.getLinkState(self.robotId,0)
#         self.positionOfLinkZero = self.stateOfLinkZero[0]
#         self.xCoordinateOfLinkZero = self.positionOfLinkZero[0]
#
#         f = open("tmp" + str(self.ID) + ".txt", "w")
#         f.write(str(self.xCoordinateOfLinkZero))
#         f.close()
#
#         os.system("mv tmp" + str(self.ID) + ".txt fitness" + str(self.ID) + ".txt")
#
#         # print(self.xCoordinateOfLinkZero)
#         pass

import pybullet as p
import pyrosim.pyrosim as pyrosim
import os
from sensor import SENSOR
from motor import MOTOR
import constants as c
import numpy
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:
    def __init__(self, SolutionID):
        # Initialize the robot with an ID
        self.ID = SolutionID
        self.robotId = p.loadURDF("robot.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)

        # Prepare to sense and act
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        # Setup the neural network
        filename = f"brain{self.ID}.nndf"
        filepath = os.path.join("/Users/jessica/Desktop/robotics2", filename)

        # Ensure the brain file is created if missing
        if not os.path.exists(filepath):
            print(f"Creating missing brain file: {filepath}")
            pyrosim.Start_NeuralNetwork(filepath)
            # Add sensor and motor neurons
            pyrosim.End()

        self.nn = NEURAL_NETWORK(filepath)

    def Prepare_To_Sense(self):
        # Prepare the sensors and ensure proper initialization
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

        # Ensure key sensor links are defined
        required_links = ['BackLowerLeg']  # Add other required links
        for link in required_links:
            if link not in pyrosim.linkNamesToIndices:
                print(f"Warning: '{link}' not defined in linkNamesToIndices.")

    def Prepare_To_Act(self):
        # Prepare the motors for the robot
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Sense(self, t):
        # Get sensor values at time 't'
        for sensor in self.sensors.values():
            sensor.Get_Value(t)

    def Act(self, t):
        # Actuate motors based on neural network outputs
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)

    def Think(self):
        # Update the neural network
        self.nn.Update()

    def Get_Fitness(self):
        # Compute fitness based on the robot's position
        self.stateOfLinkZero = p.getLinkState(self.robotId, 0)
        self.positionOfLinkZero = self.stateOfLinkZero[0]
        self.xCoordinateOfLinkZero = self.positionOfLinkZero[0]

        # Save fitness to a file
        with open(f"tmp{self.ID}.txt", "w") as f:
            f.write(str(self.xCoordinateOfLinkZero))

        # Rename temporary fitness file to final fitness file
        os.system(f"mv tmp{self.ID}.txt fitness{self.ID}.txt")
