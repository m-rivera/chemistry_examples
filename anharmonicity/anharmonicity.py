"""Anharmonicity"""
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.constants import c, h, pi, value
import numpy as np

# parameters
m1 = 1.00794  # mass of the first atom
m2 = 35.453  # mass of the second atom
we = 298700  # ωe in m-1
wexe = 5281.86  # ωexe in m-1
re = 1.27455e-10  # equilibrium bond length in m
rmax = 0.6e-9  # maximum internuclear separation in m

# equations
atomic_mass_constant = value("atomic mass constant")
red_mass = (m1 * m2) / (m1 + m2) * atomic_mass_constant  # equation for reduced mass
k = red_mass * (we * 2 * pi * c) ** 2  # equation for force constant
De = (we ** 2) / (4 * wexe)  # equation for well depth
a = np.sqrt((2 * (pi ** 2) * red_mass * c * (we ** 2)) / (h * De))  # equation for a

x = np.linspace(-re, rmax, 1000)
r = x + re  # converts displacement to internuclear separation

harmonic = (0.5 * k * x ** 2) / (h * c * De)  # equation for harmonic potential
morse = (1 - np.exp(-a * x)) ** 2  # equation for morse potential

# plotting
fig, ax = plt.subplots()
ax.plot(r, harmonic, label="Harmonic potential")
ax.plot(r, morse, label="Morse potential")
ax.plot(
    [r[0], r[-1]],
    [1, 1],
    color="grey",
    linestyle="dashed",
    label="$D_0$ = " + str(round(De / 100)) + " $cm^{-1}$",
)
ax.set_ybound(0, 2)
ax.set_xbound(0, rmax)
ax.set_ylabel("Potential energy, $V/hcD_e$")
ticks = ticker.FuncFormatter(lambda x, pos: "{0:g}".format(x * 1e9))
ax.xaxis.set_major_formatter(ticks)
ax.set_xlabel("Internuclear separation, $r$ ($nm$)")
ax.legend()

plt.show()