# Pressure/Volume vs Mole Fraction (Thermodynamics)
import matplotlib.pyplot as plt

A_star = 20
B_star = 15
y_axis = 'p'

if y_axis.lower() == 'p':
    label =  'Pressure (Pa)'
elif y_axis.upper() == 'V':
    label =  'Volume (cm\u00b3)'
else:
    label = None

