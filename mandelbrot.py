import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from PIL import Image

# Function to generate the Mandelbrot set
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Define the colormap
colors = [(0, "black"), (0.5, "purple"), (1, "orange")]
cmap = LinearSegmentedColormap.from_list("custom", colors, N=max_iter)

# Define the image size, maximum number of iterations, and bounds of the Mandelbrot set segment
img_size = (1200, 1200)
max_iter = 200
bounds = (-0.75, -0.5, -0.375, -0.125)  # (xmin, xmax, ymin, ymax)

# Generate the Mandelbrot set image
mandelbrot_set = np.zeros(img_size)
for i, real in enumerate(np.linspace(bounds[0], bounds[1], img_size[0])):
    for j, imag in enumerate(np.linspace(bounds[2], bounds[3], img_size[1])):
        mandelbrot_set[i, j] = mandelbrot(complex(real, imag), max_iter)

# Normalize the Mandelbrot set image to [0, 1] range
mandelbrot_set = mandelbrot_set / np.max(mandelbrot_set)

# Apply the colormap to the Mandelbrot set image
colored_mandelbrot_set = cmap(mandelbrot_set)

# Display the Mandelbrot set image
plt.imshow(mandelbrot_set, cmap=cmap)
plt.axis("off")
plt.show()

# Save the image as a PNG file
plt.imsave("mandelbrot_set.png", mandelbrot_set, cmap=cmap)
