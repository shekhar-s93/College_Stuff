
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='^', linestyle='-', color='g', label='Line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('48-Shekhar Suman \n Line Plot')
plt.legend()
plt.show()
