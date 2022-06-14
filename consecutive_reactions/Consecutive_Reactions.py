# Consecutive Reactions
import matplotlib.pyplot as plt
import numpy as np

k1 = 0.1    # k1 is the rate constant for the first reaction (A->B)
k2 = 1    # k2 is the rate constant for the second reaction (B->C)
t_end = 100   # t_end is the time period to be plotted
A0 = 1    # A0 is the initial concentration of A

fig, ax = plt.subplots()    # Create a figure and a 3D axes

t = np.linspace(0,t_end,t_end*10)   # Create an array of time values

A = A0*np.exp(-k1*t)    # Calculate the concentration of A using the values of t, A0 and k1
ax.plot(t,A,label='[A]')    # Plot the concentration of A

B = ((k1*A0)/(k2-k1))*(np.exp(-k1*t)-np.exp(-k2*t))   # Calculate the concentration of B using the values of t, A0, k1 and k2
ax.plot(t,B,label='[B]')    # Plot the concentration of B

C = A0 - A - B  # Calculate the concentration of C from A0, A and B
ax.plot(t,C,label='[C]')    # Plot the concentration of C

ax.legend()   # Add a legend to the figure
ax.vlines(np.log(k2/k1)/(k2-k1),0,1,color='grey',linestyles='dashed',label='[B]')   # Add a vertical line to the figure at the peak concentration of B
ax.set_xlabel('Time / s')   # Set the x label of the figure
ax.set_xbound(0,t_end)  # Set the x axis bounds
ax.set_ylabel('[A], [B], [C] / arbitrary units')    # Set the y label of the figure
ax.set_ybound(0,A0) # Set the y axis bounds

plt.show()  # Display the figure