#Consecutive Reactions
import matplotlib.pyplot as plt
import numpy as np

k1 = 0.1
k2 = 1

A0 = 1
t_end = 100

fig, ax = plt.subplots()

t = np.linspace(0,t_end,t_end*10)
A = A0*np.exp(-k1*t)
ax.plot(t,A,label='[A]')

ax.legend()
plt.show()