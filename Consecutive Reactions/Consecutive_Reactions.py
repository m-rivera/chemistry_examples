#Consecutive Reactions
import matplotlib.pyplot as plt
import numpy as np

k1 = 0.1
k2 = 1
t_end = 100

A0 = 1

fig, ax = plt.subplots()

t = np.linspace(0,t_end,t_end*10)
A = A0*np.exp(-k1*t)
ax.plot(t,A,label='[A]')

B = ((k1*A)/(k2-k1))*(np.exp(-k1*t)-np.exp(-k2*t))
ax.plot(t,B,label='[B]')

C = A0 - A - B
ax.plot(t,C,label='[C]')

ax.legend()
ax.set_xlabel('Time / s')
ax.set_xbound(0,t_end)
ax.set_ylabel('[A], [B], [C] / arbitrary units')
ax.set_ybound(0,A0)
plt.show()