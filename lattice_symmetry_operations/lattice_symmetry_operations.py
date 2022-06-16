# Symmetry Operations (Crystallography)
import matplotlib.pyplot as plt

initial_coords = [1, 2, 3]    # Initial coordinates of the atom
x, y, z = initial_coords

sym_operation = [x,x+y,y-z]   # Symmetry operation
x2,y2,z2 = sym_operation

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
max = max([x, y, z, x2, y2, z2])
ax.plot([-max, max], [0, 0], [0, 0], color='k')
ax.plot([0, 0], [-max, max], [0, 0], color='k')
ax.plot([0, 0], [0, 0], [-max, max], color='k')
ax.plot(x, y, z, marker="o", markersize=5, color='green',
        label='Initial')
ax.plot([0, x], [0, 0], [0, 0], color='green',linestyle='dashed')
ax.plot([x, x], [0, y], [0, 0], color='green',linestyle='dashed')
ax.plot([x, x], [y, y], [0, z], color='green',linestyle='dashed')
ax.plot(x2, y2, z2, marker="o",
        markersize=5, color='red', label='Final')
ax.plot([0, x2], [0, 0], [0, 0], color='red',linestyle='dashed')
ax.plot([x2, x2], [0, y2], [0, 0], color='red',linestyle='dashed')
ax.plot([x2, x2], [y2, y2], [0, z2], color='red',linestyle='dashed')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()

plt.show()
