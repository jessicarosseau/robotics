import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK


class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        self.nn = NEURAL_NETWORK("brain.nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, i):
        for sensor in self.sensors.values():
            sensor.Get_Value(i)

    def Prepare_To_Act(self):
        # self.motors = {}
        #
        # for jointName in pyrosim.jointNamesToIndices:
        #     self.motors[jointName] = MOTOR(jointName)
        #     print(jointName)
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            decodedJointName = jointName.decode('utf-8') if isinstance(jointName, bytes) else jointName
            self.motors[decodedJointName] = MOTOR(decodedJointName)
            print(f"Adding motor for joint: {decodedJointName}")

    def Act(self, i):
        # for neuronName in self.nn.Get_Neuron_Names():
        #     if self.nn.Is_Motor_Neuron(neuronName):
        #         jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
        #         desiredAngle = self.nn.Get_Value_Of(neuronName)
        #         self.motors[jointName].Set_Value(self.robotId, desiredAngle)
        #         #self.robot.Set_Motor_Value(jointName,, desiredAngle)
        #         print(neuronName, jointName, desiredAngle)

        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                if isinstance(jointName, bytes):
                    jointName = jointName.decode('utf-8')
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                if jointName in self.motors:
                    self.motors[jointName].Set_Value(self.robotId, desiredAngle)
                else:
                    print(f"Error: {jointName} not found in motors.")

        # for motor in self.motors.values():
        #     motor.Set_Value(self.robotId, i)

    def Think(self):
        self.nn.Update()
        self.nn.Print()