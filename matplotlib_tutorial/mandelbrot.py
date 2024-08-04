# The Mandelbrot Set
# zn = z² + c
#  where: 
#          c is a point in the complex plane
#          start z with 0, and iteratively find z
#          if the series diverges |z| > 2 we discard the point
#          otherwise the point corresponding to c is included in the set
#
# Algorithm:
# https://www.math.univ-toulouse.fr/~cheritat/wiki-draw/index.php/Mandelbrot_set
#
# Implementations:
# https://rosettacode.org/wiki/Mandelbrot_set#Python

import numpy as np
import matplotlib.pyplot as plt
import math

image_x = 400
image_y = 300

mesh_x = np.linspace(-2.5, 1.5, num = image_x + 1)
mesh_y = np.linspace(-1.5, 1.5, num = image_y + 1)

# Initialize the image
image = np.zeros((len(mesh_y), len(mesh_x)))


for i, y in enumerate(mesh_y):
    for j, x in enumerate(mesh_x):
        cr, ci = x, y
        zr, zi = 0, 0
        count = 0
        color = 'black'
        while count <= 50:
            count = count + 1
            z_mod_sq = zr*zr + zi*zi
            if z_mod_sq > 4:
                color = 'white'
                break
            # zr + I zi = zr² - zi² + 2*zr*zi I + cr + I ci
            zr, zi = (zr*zr - zi*zi + cr), (2*zr*zi + ci)
        if color != 'white':
            image[i][j] = 1
        else:
            # image[i][j] = count
            image[i][j] = int(math.sin(count) * 10)

plt.imshow(image, cmap=plt.cm.binary)
plt.show()
