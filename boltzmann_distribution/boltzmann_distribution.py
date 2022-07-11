"""Boltzmann Distribution"""
import matplotlib.pyplot as plt
import numpy as np
import colour
import scipy.constants as const
import random

occ=np.array([])
average =np.array([])
for i in range(1000):
    point = random.expovariate(-0.1*const.eV/(const.k*2980))
    occ = np.append(occ,point)
    average = np.append(average,np.mean(occ))

print(occ)
fig, ax = plt.subplots()
ax.plot(occ, label='Occupation')
ax.plot(average, label='Rolling average')
ax.hist(occ,bins=50,orientation='horizontal')
print(average)

ax.set_xlabel('Counts / Samples')
ax.set_ylabel('Occupation')
ax.legend()
plt.show()