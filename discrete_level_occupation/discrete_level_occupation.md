# Discrete level occupation

The following Python script will plot the occupation of evenly spaced energy levels within a given temperature range.

The script modifies the equation from the lecture material to give occupancy as a fraction:
$$\frac{n_i}{N} = \frac{g_ie^-\frac{e_i}{kT}}{N}$$

## How to use the script

Various parameters can be adjusted: 
- T\_min - lower bound for the temperature axis (Note: $T\neq0$, use 1e-30 instead).
- T\_max - upper bound for the temperature axis.
- degeneracies - degeneracies of each energy level. To change the number of levels, add additional values for degeneracy (e.g. [1, 2, 3, 4, 5, 6]).
- separation - separation between energy levels.

Running the script by clicking Activate, followed by Run, will produce a plot.

## Things to try

1. Read the script and take note of the parameters and formulae. Run the code. Why does the second energy level have a maximum?
2. Increase the degeneracy of one of the levels to 2. What happens to its occupancy? Likewise, what happens to the occupancy of the other levels?
3. Change the number of energy levels. What happens to the occupancy?