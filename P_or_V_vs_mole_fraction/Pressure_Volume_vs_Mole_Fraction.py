# Pressure/Volume vs Mole Fraction (Thermodynamics)
import matplotlib.pyplot as plt

A_star = 20  # Partial pressure/volume of pure A
B_star = 15  # Partial pressure/volume of pure B
y_axis = 'p'    # Whether the y-axis is p or V

if y_axis.lower() == 'p':
    label = 'Pressure'  # Label for the y-axis
elif y_axis.upper() == 'V':
    label = 'Volume'   # Label for the y-axis
else:
    label = None

fig, ax = plt.subplots()
# Plots a green line between (0,B_star) and (1,0)
ax.plot([0, 1], [B_star, 0], color='#555F32', label='$'+y_axis+'_B$')
# Plots a purple line between (0,0) and (1,A_star)
ax.plot([0, 1], [0, A_star], color='#5F0F5F', label='$'+y_axis+'_A$')
ax.plot([0, 1], [B_star, A_star], color='k', label='Total '+label+' $' +
        y_axis+'$')  # Plots a black line between (0,B_star) and (1,A_star)

ax.set_xlabel('Mole Fraction of A  $x_A$')
ax.set_ylabel(label+'  $'+y_axis+'$')
ax.set_xbound(0, 1)
ax.set_ybound(0)
ax.legend()

plt.show()
