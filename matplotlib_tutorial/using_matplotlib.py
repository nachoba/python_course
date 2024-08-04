# Using Matplotlib
# ================
#
# Quick Start Guide
# _________________
#
# Matplotlib graphs your data on Figures, each of which can contain one or more
# Axes, and area where points can be specified in terms of x-y coordinates.
# The simplest way of creating a Figure with an Axes is using:
#
# pyplot.subplots()
#
# We can the use Axes.plot() to draw some data on the Axes, and show() to 
# display the figure:

import matplotlib.pyplot as plt
import numpy as np


# Create a figure containing a single Axes
fig, ax = plt.subplots()

# Plot some data on the Axis
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])

# Show the figure
plt.show()
