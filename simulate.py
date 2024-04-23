# #
# import sys
# from simulation import SIMULATION
#
# # Check if the required number of arguments is provided
# if len(sys.argv) > 3:
#     directOrGUI = sys.argv[1]
#     solutionID = sys.argv[2]
#     frequency = float(sys.argv[3])
#     duration = int(sys.argv[4])  # Parse the duration correctly
# else:
#     # Default values for each parameter
#     directOrGUI = 'GUI'
#     solutionID = '0'
#     frequency = 1.0  # Default frequency
#     duration = 10000  # Default duration (in milliseconds or simulation steps)
#
# # Initialize the simulation with the provided or default parameters
# simulation = SIMULATION(directOrGUI, solutionID, frequency, duration)
#
# # Run the simulation and retrieve the fitness
# simulation.Run()
# simulation.Get_Fitness()



#
# #
#
# from simulation import SIMULATION
# import sys
#
# # Command Line Arguments
#
# if len(sys.argv) > 2:
#     directOrGUI = sys.argv[1]
#     solutionID = sys.argv[2]
#     frequency = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0  # Default frequency is 1.0
#
# simulation = SIMULATION(directOrGUI, solutionID, frequency, duration)
# simulation.Run()
# simulation.Get_Fitness()
#
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
#
#

import sys
from simulation import SIMULATION

# Default values for command-line arguments
default_frequency = 1.0
default_duration = 1000  # Provide a sensible default duration

# Check command-line arguments and set variables
if len(sys.argv) > 3:
    directOrGUI = sys.argv[1]
    solutionID = sys.argv[2]
    frequency = float(sys.argv[3]) if len(sys.argv) > 3 else default_frequency
    duration = int(sys.argv[4]) if len(sys.argv) > 4 else default_duration  # Ensure correct handling of duration
else:
    # Use default values if insufficient arguments are provided
    directOrGUI = 'GUI'
    solutionID = '0'
    frequency = default_frequency
    duration = default_duration

# Initialize simulation with correct arguments
simulation = SIMULATION(directOrGUI, solutionID, frequency, duration)
simulation.Run()
simulation.Get_Fitness()


