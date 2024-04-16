# from parallelHillClimber import PARALLEL_HILL_CLIMBER
# import os
#
#
# phc = PARALLEL_HILL_CLIMBER()
# phc.Evolve()

from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os
import subprocess
def run_simulation_with_frequency(frequency):
    # Set a longer duration for better video capture
    long_duration = 1000  # Adjust this value as needed for your videos
    subprocess.call(['python', 'simulate.py', 'GUI', '0', str(frequency), str(long_duration)])

phc = PARALLEL_HILL_CLIMBER()
frequencies = [0.5, 2.0]  # Example frequencies
for freq in frequencies:
    run_simulation_with_frequency(freq)
phc.Evolve()

