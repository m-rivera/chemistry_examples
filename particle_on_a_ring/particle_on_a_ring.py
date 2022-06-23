"""Particle On A Ring"""
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# parameters
r = 1
ml = 10

# equations
points = 270*ml # number of points to be plotted
phi = np.linspace(0, 2*np.pi, points)
psi = np.cos(ml * phi)  # real (cosine) parts of the wavefunction
x = r * np.cos(phi) # converts from polar to cartesian coordinates
y = r * np.sin(phi) # converts from polar to cartesian coordinates

# plotting
fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))
ax.scatter(x, y, psi, c=x - y)
for i in range(len(x) - 1):
    verts = [(x[i], y[i], psi[i]), (x[i + 1], y[i + 1], psi[i + 1])] + [
        (x[i + 1], y[i + 1], np.zeros(points)[i + 1]),
        (x[i], y[i], np.zeros(points)[i]),
    ]
    ax.add_collection3d(
        Poly3DCollection([verts], color="grey", linewidths=0, alpha=0.5)
    )
ax.plot(x, y, np.zeros(points), color="grey")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$\cos m_l\phi$")

plt.show()