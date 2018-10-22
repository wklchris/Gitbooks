import numpy as np
import matplotlib.pyplot as plt

r = 2
fig, ax = plt.subplots(1, 1, subplot_kw=dict(projection='polar'))

for theta in np.linspace(0, np.pi, 9):
    x = [theta, theta + np.pi]
    y = [r, r]
    ax.plot(x, y, color="k", linestyle="--")

plt.show()
