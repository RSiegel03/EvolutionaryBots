import numpy as np
import matplotlib.pyplot as plt

# load data
backLegSensorValues = np.load("data/backLegSensorValues.npy")
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")


# visualize
plt.plot(backLegSensorValues, label="Back Leg", lw=2)
plt.plot(frontLegSensorValues, label="Front Leg")

# annotate
plt.legend()
# plt.show()
plt.savefig("../HW_Sensor_Values_Plotted.png")