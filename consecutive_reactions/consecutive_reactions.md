# Consecutive reactions

The following Python script will plot the concentrations of molecules A, B and C in a pair consecutive reactions.
$$A\longrightarrow B\longrightarrow C$$
The script uses equations from the lecture material to plot $[A]_t$ (blue), $[B]_t$ (orange) and $[C]_t$ (green).
$$[A]_t = [A]_0e^{-k_1t}$$
$$[B]_t = \frac{k_1[A]_0}{k_2-k_1}(e^{-k_1t}-e^{-k_2t})$$
$$[C]_t = [A]_0-[A]_t-[B]_t$$
A dotted line is also plotted to show the time at which $[B]$ is highest ($t_{max}$).
$$t_{max} = \frac{\ln \frac{k_2}{k_1}}{k_2-k_1}$$

## How to use the script

Parameters for $k_1$ (k1) and $k_2$ (k2) can be adjusted in the script. Likewise, the initial concentration of A, $[A]_0$ (A0) can be changed. Running the script by clicking Activate, followed by Run, will produce a plot. If the x-axis is too long/short, try adjusting the run time, $t_{max}$ (t_end).

## Things to try

Read the script and take note of the parameters and formulae. Run the script.

Adjust the values of $k_1$ and $k_2$ to where $k_1>>k_2$ and $k_1<<k_2$. Make predictions of what the plot should look like and run the script.

Now set $k_1=k_2$. Run the script. Why do you get the result you do?