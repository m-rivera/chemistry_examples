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
ax.plot(x, y, z, marker="o", markersize=5, color='green')
ax.plot(final_coords[0], final_coords[1], final_coords[2], marker="o", markersize=5, color='red')
ax.plot(0, 0, 0, marker="o", markersize=5, color='grey')

plt.show()