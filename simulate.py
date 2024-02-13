import pybullet as p
import time
import pybullet_data
import numpy
import os

from pyrosim import pyrosim

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(10000)


#p.loadSDF("world.sdf")
for i in range(1000):
	p.stepSimulation()
	#backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	time.sleep(1/60)
	#print(backLegTouch)

p.disconnect()
print(backLegSensorValues)
subdirectory = 'data'

if not os.path.exists(subdirectory):
    os.makedirs(subdirectory)
filename = os.path.join(subdirectory, 'backLegSensorValues.npy')
numpy.save(filename, backLegSensorValues)
#exit()