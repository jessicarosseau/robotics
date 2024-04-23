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
    #subprocess.Popen(['python', 'simulate.py', 'GUI', '0', str(frequency), str(long_duration)])
    subprocess.call(['python', 'simulate.py', 'GUI', '0', str(frequency), str(long_duration)])

phc = PARALLEL_HILL_CLIMBER()
frequencies = [0.5, 1.0, 2.0, 5.0, 10.0]  # Example with additional frequencies
 # Example frequencies
for freq in frequencies:
    print(f"Running simulation with frequency: {freq}")
    run_simulation_with_frequency(freq)
print("Evolving with Parallel Hill Climber")
phc.Evolve()


