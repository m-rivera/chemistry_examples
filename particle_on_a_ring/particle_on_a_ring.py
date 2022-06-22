"""Particle On A Ring"""
import matplotlib.pyplot as plt
import numpy as np

# parameters
r = 2
ml = -1

# equations
phi = np.linspace(0,360,10000)
#psi = (1/np.sqrt(360))*np.exp(1j*ml*phi)
psi = np.cos(ml*phi) # real (cosine) parts of the wavefunction

# plotting
fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))
x = r*np.cos(phi)
y = r*np.sin(phi)
lines = np.linspace(0,360,360)
for line in lines:
    ax.plot([r*np.cos(line),r*np.cos(line)],[r*np.sin(line),r*np.sin(line)],[0,np.cos(ml*line)],alpha=0.3,color='grey')
ax.scatter(x,y,psi,c=x-y)
ax.plot(x,y,np.zeros(10000),alpha=0.9,color='grey')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$\cos m_l\phi$')

plt.show()