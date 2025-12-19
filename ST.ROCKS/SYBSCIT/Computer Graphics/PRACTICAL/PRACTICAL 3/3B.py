import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()

ax.add_patch(patches.Rectangle((0.1, 0.1), 0.8, 0.6, edgecolor='black', facecolor='tan'))
ax.add_patch(patches.Rectangle((0.35, 0.6), 0.3, 0.1, edgecolor='black', facecolor='saddlebrown'))

roof = plt.Polygon([(0.1, 0.7), (0.5, 1.0), (0.9, 0.7)], edgecolor='black', facecolor='firebrick')
ax.add_patch(roof)

ax.add_patch(patches.Rectangle((0.45, 0.1), 0.1, 0.3, edgecolor='black', facecolor='sienna'))

ax.add_patch(patches.Rectangle((0.2, 0.5), 0.2, 0.2, edgecolor='black', facecolor='lightblue'))
ax.add_patch(patches.Rectangle((0.6, 0.5), 0.2, 0.2, edgecolor='black', facecolor='lightblue'))

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

ax.axis('off')

plt.title('48 - SHEKHAR SUMAN \n DRAW A HUT')
plt.show()
