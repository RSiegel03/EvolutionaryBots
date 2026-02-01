import numpy as np
import matplotlib.pyplot as plt

# load data
# backLegSensorValues = np.load("data/backLegSensorValues.npy")
# frontLegSensorValues = np.load("data/frontLegSensorValues.npy")


# # visualize
# plt.plot(backLegSensorValues, label="Back Leg", lw=2)
# plt.plot(frontLegSensorValues, label="Front Leg")

# # annotate
# plt.legend()
# # plt.show()
# plt.savefig("../HW_Sensor_Values_Plotted.png")

#=============================================================================
# analyze motor data
targetAngles_backleg = np.load("data/targetAngles_backleg.npy")
targetAngles_frontleg = np.load("data/targetAngles_frontleg.npy")

plt.plot(targetAngles_backleg, label="Target Angles Backleg", color='green')
plt.plot(targetAngles_frontleg, label="Target Angles Frontleg", color='blue')
plt.legend()
plt.show()