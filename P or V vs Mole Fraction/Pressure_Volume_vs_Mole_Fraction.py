# Pressure/Volume vs Mole Fraction (Thermodynamics)
import matplotlib.pyplot as plt

A_star = 20
B_star = 15
y_axis = 'p'

if y_axis.lower() == 'p':
    label =  'Pressure'
elif y_axis.upper() == 'V':
    label =  'Volume'
else:
    label = None

fig, ax = plt.subplots()
ax.plot([0,1], [B_star,0], color='#555F32', label='$'+y_axis+'_B$')
ax.plot([0,1], [0,A_star], color='#5F0F5F', label='$'+y_axis+'_A$')
ax.plot([0,1], [B_star,A_star], color='k', label='Total '+label+' $'+y_axis+'$')

ax.set_xlabel('Mole Fraction of A $x_A$')
ax.set_ylabel(label+'  $'+y_axis+'$')
ax.set_xbound(0,1)
ax.set_ybound(0)
ax.legend()
plt.show()