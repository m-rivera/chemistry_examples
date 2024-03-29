"""Lever Rule (Thermodynamics)"""
import matplotlib.pyplot as plt
import numpy as np

# parameters
pA_star = 15  # partial pressure of pure A
pB_star = 5  # partial pressure of pure B
units = "Pa"  # units


# equations
pA = np.linspace(0, pA_star, 100)  # partial pressure of A
pB = np.linspace(pB_star, 0, 100)  # partial pressure of B
p = pA + pB  # total pressure
xA = np.linspace(0.0000000001, 1, 100)
yA = pA / p
zA = xA + ((yA - xA) / (1 + (xA / yA)))

# plotting
fig, ax = plt.subplots()
# plots a blue line for xA against p
ax.plot(xA, p, color="teal", label="$x_A$")
# plots an orange line for yA against p
ax.plot(yA, p, color="darkorange", label="$y_A$")
# plots a dashed line for zA against p
ax.plot(zA, p, color="grey", label="$z_A$", linestyle="dashed")
ax.set_xlabel("Mole Fraction of A  $z_A$")
ax.set_ylabel("Pressure  $p$ (" + units + ")")
ax.set_xbound(0, 1)
ax.set_ybound(0)
ax.legend()

plt.show()