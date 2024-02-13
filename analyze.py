import numpy as np
import os
import matplotlib.pyplot as plt

back = os.path.join('data', 'backLegSensorValues.npy')
front = os.path.join('data', 'frontLegSensorValues.npy')

backLegSensorValues = np.load(back)
frontLegSensorValues = np.load(front)

# Plotting with labels
plt.plot(backLegSensorValues, label='Back Leg', linewidth=2.5)
plt.plot(frontLegSensorValues, label='Front Leg')

# Adding a legend with the specified labels
plt.legend()

# Display the plot
plt.show()

