"""Boltzmann Distribution"""
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import k, eV

# parameters
T = None # temperature (K)
T_min = None # min temperature (K)
T_max = None # max temperature (K)

epsilon_i = None # energy state (eV)
epsilon_0 = None # lowest energy state (eV)
epsilon_i_max = None # energy state boundary (eV)


if T == epsilon_i == None:
    if T_min <= 0:
        T_min = 1e-50
    T = np.linspace(T_min,T_max,10000)
    epsilon_i = np.linspace(epsilon_0,epsilon_i_max,10000)
    T, epsilon_i = np.meshgrid(T,epsilon_i)
    # equation
    rel_occupation = np.exp(-(epsilon_i-epsilon_0)/(k/eV*T))
    # plotting
    fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
    ax.set_xlabel('Temperature, $T$ (K)')
    ax.set_ylabel('Energy state, $\epsilon_i$ (eV)')
    ax.set_zlabel(r'Relative occupation, $\dfrac{n_i}{n_0}$')
    ax.plot_surface(T,epsilon_i,rel_occupation,cmap=cm.viridis,alpha=0.9)

elif T == None:
    if T_min <= 0:
        T_min = 1e-50
    T = np.linspace(T_min,T_max,10000)
    # equation
    rel_occupation = np.exp(-(epsilon_i-epsilon_0)/(k/eV*T))
    # plotting
    fig, ax = plt.subplots()
    ax.set_xlabel('Temperature, $T$ (K)')
    ax.set_ylabel(r'Relative occupation, $\dfrac{n_i}{n_0}$')
    ax.plot(T,rel_occupation,label='$\epsilon_i='+str(epsilon_i)+'$ eV')
    ax.legend()

elif epsilon_i == None:
    epsilon_i = np.linspace(epsilon_0,epsilon_i_max,10000)
    # equation
    rel_occupation = np.exp(-(epsilon_i-epsilon_0)/(k/eV*T))
    # plotting
    fig, ax = plt.subplots()
    ax.set_xlabel('Energy state, $\epsilon_i$ (eV)')
    ax.set_ylabel(r'Relative occupation, $\dfrac{n_i}{n_0}$')
    ax.plot(epsilon_i, rel_occupation,label='$T='+str(T)+'$ K')
    ax.legend()

plt.show()