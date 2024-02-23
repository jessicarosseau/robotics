#
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
from simulation import SIMULATION
#
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
# p.setGravity(0, 0, -9.8)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")
# pyrosim.Prepare_To_Simulate(robotId)
#
# t = numpy.linspace(0, 2 * numpy.pi, c.num_steps)  # Create a time array
#
# # frontLeg
# front_targetAngles = c.front_amplitude * numpy.sin(c.front_frequency * t + c.front_phaseOffset)
#
# # backLeg
# back_targetAngles = c.back_amplitude * numpy.sin(c.back_frequency * t + c.back_phaseOffset)
#
#
# # numpy.save('data/front_targetAngles.npy', front_targetAngles)
# # numpy.save('data/back_targetAngles.npy', back_targetAngles)
# # exit()
#
# backLegSensorValues = numpy.zeros(1000)
# frontLegSensorValues = numpy.zeros(1000)
# for i in range(c.num_steps):
#     p.stepSimulation()
#
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotId,
#         jointName=b'Torso_BackLeg',
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=back_targetAngles[i],
#         maxForce=20
#     )
#
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(
#         bodyIndex=robotId,
#         jointName=b'BackLeg_FrontLeg',
#         controlMode=p.POSITION_CONTROL,
#         targetPosition=-front_targetAngles[i],
#         maxForce=20
#     )
#     time.sleep(1/240)
#
# p.disconnect()
# print(backLegSensorValues)
# print('--------------------------- \n')
# print(frontLegSensorValues)
# subdirectory = 'data'
#
# if not os.path.exists(subdirectory):
#     os.makedirs(subdirectory)
# backLegFile = os.path.join(subdirectory, 'backLegSensorValues.npy')
# frontLegFile = os.path.join(subdirectory, 'frontLegSensorValues.npy')
#
# numpy.save(backLegFile, backLegSensorValues)
# numpy.save(frontLegFile, frontLegSensorValues)
simulation = SIMULATION()