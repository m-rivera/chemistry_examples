"""Anharmonicity"""
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.constants import c, h, pi, value
import numpy as np

# parameters
m1 = 1.00794  # atomic mass of the first atom
m2 = 35.453  # atomic mass of the second atom
we = 298700  # ωe in m-1
wexe = 5281.86  # ωexe in m-1
re = 1.27455e-10  # equilibrium bond length in m
rmax = 0.6e-9  # maximum internuclear separation in m
vmax = 0

# equations
atomic_mass_constant = value("atomic mass constant")
red_mass = (m1 * m2) / (m1 + m2) * atomic_mass_constant  # equation for reduced mass
k = red_mass * (we * 2 * pi * c) ** 2  # equation for force constant
De = (we ** 2) / (4 * wexe)  # equation for well depth
a = np.sqrt((2 * (pi ** 2) * red_mass * c * (we ** 2)) / (h * De))  # equation for a

x = np.linspace(-re, rmax, 1000)
r = x + re  # converts displacement to internuclear separation
v = np.arange(vmax)
harmonic = (0.5 * k * x ** 2) / (h * c * De)  # equation for harmonic potential
morse = (1 - np.exp(-a * x)) ** 2  # equation for morse potential
Gv_harmonic = we*(v+0.5)/De
Gv_morse = (we*(v+0.5)-wexe*(v+0.5)**2)/De

# plotting
fig, ax = plt.subplots()
ax.plot(r, harmonic,color='#1E64A5', label="Harmonic potential")
for level in Gv_harmonic:
    xmin = r[np.where(harmonic < level)][0]
    xmax = r[np.where(harmonic < level)][-1]
    ax.hlines(level, xmin, xmax,color='#1E64A5')
ax.plot(r, morse,color='#FA690F', label="Morse potential")
for level in Gv_morse:
    xmin = r[np.where(morse < level)][0]
    xmax = r[np.where(morse < level)][-1]
    ax.hlines(level, xmin, xmax,color='#FA690F')
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