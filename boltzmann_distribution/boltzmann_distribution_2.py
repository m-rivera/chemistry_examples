"""Boltzmann Distribution 2"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import k, eV

# parameters
T = 40000 # temperature (K)
T_min = 1e-30 # min temperature (K)
T_max = 40000 # max temperature (K)

levels = 5
degeneracies = [1,1,1,1,1]
separation = 0.1
epsilon_0 = 0 # lowest energy state (eV)

states = np.arange(epsilon_0, epsilon_0+levels * separation,separation)
occupation = degeneracies*np.exp(-(states-epsilon_0)/(k/eV*T))
occupation = occupation/np.sum(occupation)
fig, ax = plt.subplots()
ax.bar(states,occupation,width=separation,align='edge')

T = np.linspace(T_min,T_max,500)
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
for t in T:
    occupation = degeneracies*np.exp(-(states-epsilon_0)/(k/eV*t))
    occupation = occupation/np.sum(occupation)
    ax.bar3d(x=t*np.ones(np.shape(states)),y=states,z=np.zeros(np.shape(states)),dx=(T_max-T_min)/500*np.ones(np.shape(states)),dy=separation*np.ones(np.shape(states)),dz=occupation,color='#1E64A5',alpha=0.5)
ax.view_init(elev=15,azim=120)
plt.show()
