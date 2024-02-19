# import pybullet as p
# import time
# import pybullet_data
# import numpy
# import os
#
# from pyrosim import pyrosim
#
# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())
#
# p.setGravity(0,0,-9.8)
#
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
#
# pyrosim.Prepare_To_Simulate(robotId)
#
#
# backLegSensorValues = numpy.zeros(10000)
# frontLegSensorValues = numpy.zeros(1000)
# #p.loadSDF("world.sdf")
# for i in range(1000):
# 	p.stepSimulation()
# 	#backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
# 	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
# 	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
# 	time.sleep(1/60)
# 	#print(backLegTouch)
#
# p.disconnect()
# print(backLegSensorValues)
# print('/n')
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
import math

import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import os

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setGravity(0, 0, -9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b'Torso_BackLeg',
        controlMode=p.POSITION_CONTROL,
        targetPosition= +math.pi/4.0,
        maxForce=500)
    time.sleep(1/60)

p.disconnect()
print(backLegSensorValues)
print(frontLegSensorValues)
subdirectory = 'data'

if not os.path.exists(subdirectory):
    os.makedirs(subdirectory)
backLegFile = os.path.join(subdirectory, 'backLegSensorValues.npy')
frontLegFile = os.path.join(subdirectory, 'frontLegSensorValues.npy')

numpy.save(backLegFile, backLegSensorValues)
numpy.save(frontLegFile, frontLegSensorValues)