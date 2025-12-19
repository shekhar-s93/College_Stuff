import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

ax.axhline(0, color='black', lw=2)

ax.axvline(0, color='black', lw=2)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

ax.set_aspect('equal', adjustable='box')

plt.title('48 SHEKHAR SUMAN \n Co-ordinate axis at center') 

plt.show()
