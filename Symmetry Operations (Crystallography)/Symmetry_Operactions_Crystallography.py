#Symmetry Operations (Crystallography)
from re import X
import matplotlib.pyplot as plt

initial_coords = [1,2,3]
sym_operation = 'x,x+y,y-z'

final_coords = [0,0,0]
sym_operation = sym_operation.split(',')
x = initial_coords[0]
y = initial_coords[1]
z = initial_coords[2]

for axis, operation in enumerate(sym_operation):
    subtract = False
    for character in operation:
        
        temp = 0
        if character == 'x':
            temp += x
        elif character == 'y':
            temp += y
        elif character == 'z':
            temp += z
    
        if subtract == True:
            temp = -temp

        final_coords[axis] += temp
        subtract = False

        if character == '-':
            subtract = True


fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.plot(x, y, z, marker="o", markersize=5, color='green', label='Initial')
ax.plot(final_coords[0], final_coords[1], final_coords[2], marker="o", markersize=5, color='red', label='Final')

max_x = max([x,final_coords[0]])
ax.plot([-max_x,max_x], [0,0], [0,0], color='k')

max_y = max([y,final_coords[1]])
ax.plot([0,0], [-max_y,max_y], [0,0], color='k')

max_z = max([z,final_coords[2]])
ax.plot([0,0], [0,0], [-max_z,max_z], color='k')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()
plt.show()