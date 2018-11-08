import numpy as np
import matplotlib.pyplot as plt
import ode_toolkit.phaseplot as pp

def ff(x, y):
    dx = y
    dy = - (x ** 2) / 2 + x

    return (dx, dy)


fig, ax = plt.subplots(1, 1)
ax = pp.plot_phase2d(ax, ff, (-2, 4), (-2, 2))
ax.set_title(r"Phase plane of conservative system $dx = y, dy=-\frac{1}{2}x^2+x$")

plt.show()
