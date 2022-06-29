"""Boltzmann Distribution 2"""
import matplotlib.pyplot as plt
import numpy as np
import colour
from scipy.constants import k, eV

# parameters
T_min = 1e-30  # min temperature (K)
T_max = 40000  # max temperature (K)
levels = [1, 1, 1, 1, 1]  # degeneracies of each energy level
separation = 0.1  # separation between energy levels

# equations
energies = np.linspace(
    0, (len(levels)-1) * separation, len(levels)
)  # calculates the energies of each level
T = np.linspace(T_min, T_max, 500)

# plotting
fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))
red = colour.Color("red")
colours = list(red.range_to(colour.Color("blue"), len(levels)))
for i, c in enumerate(colours):
    colours[i] = c.rgb

# more equations
for t in T:
    occupation = levels * np.exp(
        -(energies) / (k / eV * t)
    )  # calculates occupation of each energy level
    occupation = occupation / np.sum(
        occupation
    )  # calculates occupation to make total occupation, N = 1
    ax.bar3d(
        x=t * np.ones(np.shape(energies)),
        y=energies,
        z=np.zeros(np.shape(energies)),
        dx=(T_max - T_min) / 500 * np.ones(np.shape(energies)),
        dy=separation * np.ones(np.shape(energies)),
        dz=occupation,
        color=colours,
    )

# more plotting
ax.set_xlabel("Temperature, $T$ (K)")
ax.set_ylabel("Energy level (eV)")
ax.set_zlabel(r"Energy level occupation, $\frac{n}{N}$")
ax.view_init(elev=7.5, azim=120)

plt.show()
