from simulation import SIMULATION
import sys

# Command Line Arguments

if len(sys.argv) > 1:
    directOrGUI = sys.argv[1]
else:
    directOrGUI = 'GUI'

simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()


