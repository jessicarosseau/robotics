import pyrosim.pyrosim as pyrosim


def Create_World():
     pyrosim.Start_SDF("world.sdf")
     pyrosim.Send_Cube(name="Box", pos=[-2, -2, .5], size=[1, 1, 1])
     pyrosim.End()

def Create_Body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0, .5, 0.5], size=[1, 1, 1])

    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[.5, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[.5, .5, .5], size=[1, 1, 1])


    pyrosim.Send_Joint(name="BackLeg_FrontLeg", parent="BackLeg", child="FrontLeg", type="revolute", position=[1, 0, 0])
    pyrosim.Send_Cube(name="FrontLeg", pos=[.5, .5, -.5], size=[1, 1, 1])
    pyrosim.End()

def Create_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    pyrosim.End()


Create_Body()
Create_Brain()






