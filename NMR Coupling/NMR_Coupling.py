#NMR Coupling Visualiser
import matplotlib.pyplot as plt
import numpy as np
import math

n = [1,1]
J_coupling_constants = [6,2]


def function(x,positions,n_index):
    standard_deviation = 0.125
    y = 0
    coefficient = 1
    for a in n[:n_index+1]:
        coefficient = (2**a)*coefficient
    if n_index == -1:
        coefficient = 1
    for position in positions:
        y += (math.exp(-((x-position)**2)/(2*standard_deviation))/(standard_deviation*math.sqrt(2/math.pi)))/coefficient
    return y


def construct():
    positions = [0]
    for n_index in range(len(n)):
        for i in range(n[n_index]):
            for i in range(len(positions)):
                positions.append(positions[i]+J_coupling_constants[n_index]/2)
                positions[i]=positions[i]-J_coupling_constants[n_index]/2

    
fig, ax = plt.subplots()
x = np.linspace(-20,20,100)