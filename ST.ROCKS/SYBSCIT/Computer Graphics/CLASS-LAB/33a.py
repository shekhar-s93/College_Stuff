import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse  #IMported File

fig, ax = plt.subplots()

circle = plt.Circle((0.5, 0.5), 0.4, edgecolor='black', facecolor='red')
ax.add_patch(circle)

rectangle = plt.Rectangle((0.2, 0.2), 0.6, 0.4, edgecolor='black', facecolor='green')
ax.add_patch(rectangle)

square = plt.Rectangle((0.2, 0.6), 0.4, 0.4, edgecolor='black', facecolor='blue')
ax.add_patch(square)

circle_outer = plt.Circle((0.8, 0.2), 0.2, edgecolor='black', facecolor='yellow')
circle_inner = plt.Circle((0.8, 0.2), 0.1, edgecolor='black', facecolor='orange')
ax.add_patch(circle_outer)
ax.add_patch(circle_inner)

ellipse = Ellipse((0.5, 0.8), 0.4, 0.2, edgecolor='black', facecolor='purple')  # Corrected line
ax.add_patch(ellipse)

line = plt.Line2D([0.2, 0.8], [0.8, 0.8], color='black', linewidth=2)
ax.add_line(line)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')

ax.axis('off')

plt.show()
