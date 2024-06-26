import pyrosim.pyrosim as pyrosim
import numpy
import random
import os
import time
import constants as c


class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = 2 * numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) - 1
        self.weights = self.weights * c.numMotorNeurons - 1
        self.fitness = 0

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID
        nextAvailableID += 1

    def Start_Simulation(self, mode):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        #os.system("python3 simulate.py " + mode + " " + str(self.myID)+"2&>1" + " &")
        os.system("python3 simulate.py " + mode + " " + str(self.myID) + " > /dev/null 2>&1")

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)

        f = open(fitnessFileName, "r")
        self.fitness = float(f.read())
        f.close()
        os.system("rm " + fitnessFileName)

    def Mutate(self):
        row = random.randint(0, c.numSensorNeurons - 1)
        column = random.randint(0, c.numMotorNeurons - 1)

        self.weights[row, column] = 2 * (random.random() * c.numMotorNeurons - 1) - 1

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-4, 4, 0.5], size=[1, 1, 1])
        pyrosim.End()


    def Create_Body(self):
        pyrosim.Start_URDF("robot.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])

        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])

        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute",
                           position=[0, 1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute",
                           position=[0, -1, 0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute",
                           position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute",
                           position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLowerLeg")
        pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=6, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=7, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=9, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="RightLeg_RightLowerLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])

        pyrosim.End()