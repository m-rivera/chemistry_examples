# Symmetry Operations (Crystallography)
import matplotlib.pyplot as plt

initial_coords = [1, 2, 3]    # Initial coordinates of the atom
sym_operation = 'x,x+y,y-z'   # Symmetry operation

final_coords = [0, 0, 0]
# Split the symmetry operation into its x, y and z components
sym_operation = sym_operation.split(',')

x, y, z = initial_coords

# Loop through the x, y and z components of the symmetry operation
for axis, operation in enumerate(sym_operation):
    subtract = None
    for character in operation:    # Loop through the characters in the symmetry operation
        temp = 0
        if character == 'x':
            temp += x   # If the character is x, add the x coordinate to the temporary variable
        elif character == 'y':
            temp += y   # If the character is y, add the y coordinate to the temporary variable
        elif character == 'z':
            temp += z   # If the character is z, add the z coordinate to the temporary variable

        if subtract == True:
            temp = -temp    # If the previous character was a '-' then set the temp variable to negative
        # Add the temporary variable to the final coordinate
        final_coords[axis] += temp
        subtract = False
        if character == '-':
            subtract = True   # If the character is a '-' then set the subtract variable to True


fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
max = max([x, y, z, max(final_coords)])
ax.plot([-max, max], [0, 0], [0, 0], color='k')
ax.plot([0, 0], [-max, max], [0, 0], color='k')
ax.plot([0, 0], [0, 0], [-max, max], color='k')
ax.plot(x, y, z, marker="o", markersize=5, color='green',
        label='Initial')
ax.plot([0, x], [0, 0], [0, 0], color='green',linestyle='dashed')
ax.plot([x, x], [0, y], [0, 0], color='green',linestyle='dashed')
ax.plot([x, x], [y, y], [0, z], color='green',linestyle='dashed')
ax.plot(final_coords[0], final_coords[1], final_coords[2], marker="o",
        markersize=5, color='red', label='Final')
ax.plot([0, final_coords[0]], [0, 0], [0, 0], color='red',linestyle='dashed')
ax.plot([final_coords[0], final_coords[0]], [0, final_coords[1]], [0, 0], color='red',linestyle='dashed')
ax.plot([final_coords[0], final_coords[0]], [final_coords[1], final_coords[1]], [0, final_coords[2]], color='red',linestyle='dashed')


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()

plt.show()
