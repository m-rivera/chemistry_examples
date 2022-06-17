# NMR Coupling Visualiser
import matplotlib.pyplot as plt
import numpy as np
import math

n = [1, 1]  # Number of H atoms per coupling
J_coupling_constants = [6, 2]  # List of J coupling constants
standard_deviation = 0.125  # Standard deviation of the Gaussian curves


def function(x, positions, n_index):  # Function to calculate the Gaussian curves
    coefficient = 1
    for a in n[: n_index + 1]:
        # Calculate the number of curves required
        coefficient = (2 ** a) * coefficient
    y = np.zeros(len(x))  # Create an array of zeros to store the y values
    if n_index == -1:
        coefficient = 1
    for position in positions:
        y += (
            np.exp(-((x - position) ** 2) / (2 * standard_deviation))
            / (standard_deviation * math.sqrt(2 / math.pi))
        ) / coefficient  # Calculates the splitting pattern by adding together Gaussian curves
    return y  # Returns the y coordinates for the splitting pattern


fig, ax = plt.subplots()  # Create a figure and a 3D axes
x = np.linspace(-20, 20, 1000)  # Create an array of x values

positions = [0]  # List of positions for each curve
n_index = -1
# Calculate the y coordinates for the uncoupled peak
y = function(x, positions, n_index)
ax.plot(x, y, label="Uncoupled")  # Plot the uncoupled peak

label = "J = "
for n_index in range(len(n)):
    label = label + str(J_coupling_constants[n_index]) + " Hz"
    for i in range(n[n_index]):
        for i in range(len(positions)):
            positions.append(positions[i] + J_coupling_constants[n_index] / 2)
            positions[i] = positions[i] - J_coupling_constants[n_index] / 2
    # Calculate the y coordinates for each additional coupling
    y = function(x, positions, n_index)
    ax.plot(x, y, label=label)  # Plot each coupling
    label = label + ", "

ax.legend()
ax.set_xlabel("Hz")
ax.set_yticklabels([])

plt.show()
