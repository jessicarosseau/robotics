import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c
import numpy as np
import math  # Import math library to use mathematical functions


class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.runs)

    def Get_Value(self, t, frequency=1.0):  # Accept frequency as a parameter
        original_value = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        sinusoidal_value = math.sin(frequency * t)
        self.values[t] = sinusoidal_value
    # def __init__(self, linkName):
    #     self.linkName = linkName
    #     self.values = numpy.zeros(c.runs)
    #
    # def Get_Value(self, t):
    #     # Original touch sensor value
    #     original_value = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
    #
    #     # Overwrite the sensor's value with a sinusoidal signal
    #     # x is the frequency of the sinusoidal signal, adjust as needed
    #     x = 1  # You can start with x = 1 for testing purposes
    #     sinusoidal_value = math.sin(x * t)
    #
    #     # Update the sensor's value to the sinusoidal value
    #     self.values[t] = sinusoidal_value
    #
    #     # Optionally, you can blend the original sensor value with the sinusoidal signal
    #     # This could be useful if you want to maintain some touch sensor functionality
    #     # Example: self.values[t] = original_value * sinusoidal_value
    #
    # def Get_Value(self, t):
    #     original_value = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
    #     frequency = 1.0  # Default frequency, adjust as necessary
    #     sinusoidal_value = np.sin(frequency * t)
    #     self.values.append(sinusoidal_value)
