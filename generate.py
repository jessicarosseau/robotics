import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = height/2
for a in range(5):
    for b in range(5):
        pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

        for i in range(10):
            z += 1
            length = length * .9
            width = width * .9
            height = height * .9
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

        # reset
        length, width, height = 1,1,1
        z = height/2
        x += 1

    length = 1
    width = 1
    height = 1
    x = 0
    y += 1
    z = height/2


pyrosim.End()
