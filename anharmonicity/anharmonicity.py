"""Anharmonicity"""
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import scipy.constants as const
from scipy.constants import c, h, pi, value
import numpy as np

# parameters
m1 = 1.00794  # atomic mass of the first atom
m2 = 35.453  # atomic mass of the second atom
we = 298700  # ω_e in m-1
wexe = 5281.86  # ω_e x_e in m-1
re = 1.27455e-10  # equilibrium bond length in m
rmax = 0.6e-9  # maximum internuclear separation in m
n_levels = 30  # number of energy levels to be plotted

# equations
red_mass = (m1 * m2) / (m1 + m2) * const.value("atomic mass constant")  # reduced mass
k = red_mass * (we * 2 * const.pi * const.c) ** 2  # force constant
De = (we ** 2) / (4 * wexe)  # well depth
a = np.sqrt(
    (2 * (const.pi ** 2) * red_mass * const.c * (we ** 2)) / (const.h * De)
)  # equation for a in Morse potential

x = np.linspace(-re, rmax, 1000) # displacement
r = x + re  # converts displacement to internuclear separation
v = np.arange(n_levels) # vibrational quantum numbers
harmonic = (0.5 * k * x ** 2) / (const.h * const.c * De)  # harmonic potential
Gv_harmonic = we * (v + 0.5) / De  # G(v) of a harmonic oconstllator
morse = (1 - np.exp(-a * x)) ** 2  # Morse potential
Gv_morse = (we * (v + 0.5) - wexe * (v + 0.5) ** 2) / De  # G(v) of the Morse potential

# plotting
fig, ax = plt.subplots()
ax.plot(r, harmonic, color="teal", label="Harmonic potential")
for level in Gv_harmonic:
    rmin = r[np.where(harmonic < level)][0]
    rmax = r[np.where(harmonic < level)][-1]
    ax.hlines(level, rmin, rmax, color="teal")
ax.plot(r, morse, color="darkorange", label="Morse potential")
for level in Gv_morse:
    rmin = r[np.where(morse < level)][0]
    rmax = r[np.where(morse < level)][-1]
    ax.hlines(level, rmin, rmax, color="darkorange")
ax.plot(
    [r[0], r[-1]],
    [1, 1],
    color="grey",
    linestyle="dashed",
    label="$D_0$ = " + str(round(De / 100)) + " cm$^{-1}$",
)
ax.set_ybound(0, Gv_harmonic[-1])
ax.set_xbound(0, rmax)
ax.set_ylabel("Potential energy, $V/hcD_e$")
ticks = ticker.FuncFormatter(lambda x, pos: "{0:g}".format(x * 1e9))
ax.xaxis.set_major_formatter(ticks)
ax.set_xlabel("Internuclear separation, $r$ (nm)")
ax.legend()

plt.show()
