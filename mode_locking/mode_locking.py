"""Mode Locking"""
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const

# parameters
L = 30e-2  # laser cavity length (m)
N = 10  # number of cavity modes

# equations
x = np.linspace(0, 5.0000001, 10000)  # x = ct/2L
I = (np.sin(N * const.pi * x) ** 2) / (
    np.sin(const.pi * x) ** 2
)  # equation for calculating I

# plotting
fig, ax = plt.subplots()
ax.plot(x, I)
secax = ax.secondary_xaxis(
    "top",
    functions=(
        lambda x: (2 * L / const.c) * x * 10 ** 9,
        lambda x: (const.c / 2 / L) * x * 10 ** -9,
    )
)
secax.set_xlabel("Time, $t$ ($ns$)")
ax.set_xlabel("Time, $ct/2L$")
ax.set_ylabel("Intensity, $I$ ($a.u.$)")

plt.show()
