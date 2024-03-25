from simulation import SIMULATION
import sys

# Command Line Arguments

if len(sys.argv) > 1:
    directOrGUI = sys.argv[1]
else:
    directOrGUI = 'GUI'

SolutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI, SolutionID)
simulation.Run()
simulation.Get_Fitness()


