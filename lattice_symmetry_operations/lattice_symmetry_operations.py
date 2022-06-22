"""Lattice Symmetry Operations"""
import matplotlib.pyplot as plt

# parameters
initial_coords = [1, 2, 3]  # initial coordinates of the atom
x, y, z = initial_coords

sym_operator = [-x, y, z]  # symmetry operatior
x2, y2, z2 = sym_operator

# plotting
fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))
maximum = max([x, y, z, x2, y2, z2])
minimum = min([x, y, z, x2, y2, z2])
maximmum = max([maximum, -minimum])
ax.plot([-maximum, maximum], [0, 0], [0, 0], color="k")
ax.plot([0, 0], [-maximum, maximum], [0, 0], color="k")
ax.plot([0, 0], [0, 0], [-maximum, maximum], color="k")
ax.scatter(
    [x, x, -maximum], [maximum, y, y], [z, -maximum, z],
    marker="x",
    color="green",
    alpha=1,
)
ax.plot(
    x, y, z,
    marker="o",
    markersize=5,
    color="green",
    label="Initial $(" + str(x) + "," + str(y) + "," + str(z) + ")$",
)
ax.plot([0, x], [0, 0], [0, 0], color="green", linestyle="dashed")
ax.plot([x, x], [0, y], [0, 0], color="green", linestyle="dashed")
ax.plot([x, x], [y, y], [0, z], color="green", linestyle="dashed")
ax.scatter(
    [x2, x2, -maximum], [maximum, y2, y2], [z2, -maximum, z2],
    marker="x",
    color="red",
    alpha=1,
)
ax.plot(
    x2, y2, z2,
    marker="o",
    markersize=5,
    color="red",
    label="Final $(" + str(x2) + "," + str(y2) + "," + str(z2) + ")$",
)
ax.plot([0, x2], [0, 0], [0, 0], color="red", linestyle="dashed")
ax.plot([x2, x2], [0, y2], [0, 0], color="red", linestyle="dashed")
ax.plot([x2, x2], [y2, y2], [0, z2], color="red", linestyle="dashed")

ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")
ax.legend()

plt.show()