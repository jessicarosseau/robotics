import pybullet as p
import time
import pybullet_data

from pyrosim import pyrosim

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)
#p.loadSDF("world.sdf")
for i in range(1000):
	p.stepSimulation()
	backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	time.sleep(1/60)
	print(backLegTouch)

p.disconnect()
