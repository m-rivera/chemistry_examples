#NMR Coupling Visualiser
import matplotlib.pyplot as plt
import numpy as np
import math

n = [1,1]
J_coupling_constants = [6,2]


def function(x,positions,n_index):
    standard_deviation = 0.125
    coefficient = 1
    for a in n[:n_index+1]:
        coefficient = (2**a)*coefficient
    y=x-x
    if n_index == -1:
        coefficient = 1
    for position in positions:
        y += (np.exp(-((x-position)**2)/(2*standard_deviation))/(standard_deviation*math.sqrt(2/math.pi)))/coefficient
    return y

    
fig, ax = plt.subplots()
x = np.linspace(-20,20,1000)
positions = [0]
n_index = -1
y = function(x,positions,n_index)
ax.plot(x,y)
label = 'J = '
for n_index in range(len(n)):
    label = label+str(J_coupling_constants[n_index])+' Hz'
    for i in range(n[n_index]):
        for i in range(len(positions)):
            positions.append(positions[i]+J_coupling_constants[n_index]/2)
            positions[i]=positions[i]-J_coupling_constants[n_index]/2
    y = function(x,positions,n_index)
    ax.plot(x,y, label=label)
    label = label+', '
ax.legend()
ax.set_xlabel("Hz")
ax.set_yticklabels([])
plt.show()