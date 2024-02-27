import numpy
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.values = numpy.zeros(c.num_steps)

        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.offset = c.phaseOffset
        self.frequency = c.frequency
        if self.jointName == "Torso_BackLeg":
            self.frequency = c.frequency / 2
        self.values = \
            [self.amplitude * numpy.sin(self.frequency * i + self.offset)
             for i in numpy.linspace(0, 2 * c.pi, c.num_steps)]

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot.robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.values[t],
            maxForce=20)

    def Save_Values(self):
        numpy.save('data\MotorValues.npy', self.MotorValues)