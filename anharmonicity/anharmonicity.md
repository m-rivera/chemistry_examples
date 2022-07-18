# Anharmonicity

The following Python script will plot Harmonic (teal) and Morse (orange) potentials and their respective energy levels for a diatomic molecule.

The script uses equations from the lecture materials to plot the Harmonic potentials and energy levels:
$$V(x) = \frac{1}{2} kx^2$$
$$G(v) = \omega_e(v+\frac{1}{2})$$
Likewise, the Morse potentials and energy levels are calculated using:
$$V(x) = hcD_e(1-e^{-ax})^2$$
$$G(v) = \omega_e(v+\frac{1}{2})-\omega_ex_e(v+\frac{1}{2})^2$$
A dotted line is also plotted to show the dissociation limit $D_0$.

## How to use the script

Various parameters can be adjusted: 
- m1 - atomic mass of the first atom.
- m2 - atomic mass of the second atom.
- we - harmonic wavenumber.
- wexe - first anharmonic wavenumber.
- re - equilibrium bond length.
- rmax - upper bound for r used for plotting (try changing this if the x axis is too long/short).
- n\_levels - number of energy levels plotted by the script (this also controls the y-axis bounds).

Running the script by clicking Activate, followed by Run, will produce a plot.

## Things to try

1. Read the script and take note of the parameters and formulae. The defaults refer to a molecule of $\text{HCl}$. Run the code. Observe the differences between the Harmonic and Morse energy levels.
2. Adjust the number of energy levels to 5. Make predictions of what the plot should look like and run the script.
3. Change each parameter one at a time. What are their effects on the plot?
4. Find parameters for $\text{H}_2$ in the NIST database (<https://webbook.nist.gov/cgi/cbook.cgi?ID=C1333740&Mask=1000>) and alter the script. Are there any differences? If so, why?