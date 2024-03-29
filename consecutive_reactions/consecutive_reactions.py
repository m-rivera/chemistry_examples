"""Consecutive Reactions (Kinetics)"""
import matplotlib.pyplot as plt
import numpy as np

# parameters
k1 = 0.1  # k1 is the rate constant for the first reaction (A->B)
k2 = 1  # k2 is the rate constant for the second reaction (B->C)
t_end = 100  # t_end is the time period to be plotted
A0 = 1  # A0 is the initial concentration of A

# equations
t = np.linspace(0, t_end, 1000)  # create an array of time values
A = A0 * np.exp(
    -k1 * t
)  # calculate the concentration of A using the values of t, A0 and k1
B = ((k1 * A0) / (k2 - k1)) * (
    np.exp(-k1 * t) - np.exp(-k2 * t)
)  # calculate the concentration of B using the values of t, A0, k1 and k2
C = A0 - A - B  # calculate the concentration of C from A0, A and B
t_max = np.log(k2 / k1) / (k2 - k1)  # indicate the time of maximum [B]

# plotting
fig, ax = plt.subplots()
ax.plot(t, A, label="[A]")
ax.plot(t, B, label="[B]")
ax.plot(t, C, label="[C]")
ax.vlines(t_max, 0, 1, color="grey", linestyles="dashed", label="$t_{max}$")
ax.set_xlabel("Time / s")
ax.set_xbound(0, t_end)
ax.set_ylabel("[A], [B], [C] / arbitrary units")
ax.set_ybound(0, A0)
ax.legend()

plt.show()