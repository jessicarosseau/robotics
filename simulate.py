import sys
from simulation import SIMULATION

if len(sys.argv) > 3:
    directOrGUI = sys.argv[1]
    solutionID = sys.argv[2]
    frequency = float(sys.argv[3])
    duration = int(sys.argv[4])  # Make sure to parse the duration correctly
else:
    directOrGUI = 'GUI'
    solutionID = '0'
    frequency = 1.0  # default frequency
    duration = 10000  # default duration

simulation = SIMULATION(directOrGUI, solutionID, frequency, duration)
simulation.Run()
simulation.Get_Fitness()
#
#

from simulation import SIMULATION
import sys

# Command Line Arguments

# if len(sys.argv) > 2:
#     directOrGUI = sys.argv[1]
#     solutionID = sys.argv[2]
#     frequency = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0  # Default frequency is 1.0
#
# simulation = SIMULATION(directOrGUI, solutionID, frequency, duration)
# simulation.Run()
# simulation.Get_Fitness()

# if len(sys.argv) > 1:
#     directOrGUI = sys.argv[1]
# else:
#     directOrGUI = 'GUI'
#
# SolutionID = sys.argv[2]
#
# simulation = SIMULATION(directOrGUI, SolutionID)
# simulation.Run()
# simulation.Get_Fitness()


