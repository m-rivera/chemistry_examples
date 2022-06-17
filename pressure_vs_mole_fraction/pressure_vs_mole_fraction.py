"""Pressure vs Mole Fraction (Thermodynamics)"""
import matplotlib.pyplot as plt

# parameters
pA_star = 20  # partial pressure of pure A
pB_star = 15  # partial pressure of pure B
units = "Pa"  # units

# plotting
fig, ax = plt.subplots()

# plots a green line between (0,B_star) and (1,0)
ax.plot([0, 1], [pB_star, 0], color="#555F32", label="$p_B$")
# plots a purple line between (0,0) and (1,A_star)
ax.plot([0, 1], [0, pA_star], color="#5F0F5F", label="$p_A$")
# plots a black line between (0,B_star) and (1,A_star)
ax.plot([0, 1], [pB_star, pA_star], color="k", label="Total pressure $p$")
ax.set_xlabel("Mole Fraction of A  $x_A$")
ax.set_ylabel("Pressure  $p$ (" + units + ")")
ax.set_xbound(0, 1)
ax.set_ybound(0)
ax.legend()

plt.show()
