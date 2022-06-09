#Symmetry Operations (Crystallography)
from re import X
import matplotlib.pyplot as plt

initial_coords = [1,2,3]    # Initial coordinates of the atom
sym_operation = 'x,x+y,y-z'   # Symmetry operation

final_coords = [0,0,0]
sym_operation = sym_operation.split(',')    # Split the symmetry operation into its x, y and z components

x = initial_coords[0]
y = initial_coords[1]
z = initial_coords[2]

for axis, operation in enumerate(sym_operation):    # Loop through the x, y and z components of the symmetry operation
    subtract = False
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
        final_coords[axis] += temp  # Add the temporary variable to the final coordinate
        subtract = False
        if character == '-':
            subtract = True   # If the character is a '-' then set the subtract variable to True


fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))    # Create a figure and a 3D axes

ax.plot(x, y, z, marker="o", markersize=5, color='green', label='Initial')  # Plot the initial coordinates
ax.plot(final_coords[0], final_coords[1], final_coords[2], marker="o", markersize=5, color='red', label='Final')    # Plot the final coordinates

max = max([x,y,z,max(final_coords)])
ax.plot([-max,max], [0,0], [0,0], color='k')    # Draw the x axis
ax.plot([0,0], [-max,max], [0,0], color='k')    # Draw the y axis
ax.plot([0,0], [0,0], [-max,max], color='k')    # Draw the z axis

ax.set_xlabel('x')  # Set the label of the x axis
ax.set_ylabel('y')  # Set the label of the y axis
ax.set_zlabel('z')  # Set the label of the z axis
ax.legend() # Add a legend to the figure
plt.show()  # Display the figure
