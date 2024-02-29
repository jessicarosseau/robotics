import numpy
import pyrosim.pyrosim as pyrosim
import constants as c

class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.num_steps)

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        # if t == c.num_steps - 1:
        #     self.values

    def Save_Values(self):
        numpy.save('data/SensorValues.npy', self.values)