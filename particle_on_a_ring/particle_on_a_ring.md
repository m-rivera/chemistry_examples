# Particle on a ring

The following Python script will plot the real components of wavefunctions for a particle on a ring. \par\medskip 
\noindent The script uses wavefunction from the lecture material:
$$\psi (\phi) = N(\cos m_l \phi \pm i \sin m_l \phi)$$

## How to use the script

The quantum number, $m_l$, should be changed to show different wavefunctions. Running the script by clicking Activate, followed by Run, will produce a 3D plot of the wavefunction's real component.

## Things to try

1. Read the script and take note of the parameters and formulae. Run the code.

2. Make drawings of what the plots should look like for $m_l=\pm 1, \pm 2, \pm 3$ and $\pm 4$. Run the script. Were your drawings correct? 

3. EXTENSION: Change the function for psi to:  
psi = np.cos(2 * phi) * np.cos(3 * phi)}  
Run the script. What does the plot show? Are the wavefunctions for $m_l = 2$ and $m_l = 3$ orthogonal?  
(HINT: The function refers to the multiplication of the wavefunctions for $m_l = 2$ and $m_l = 3$)