import matplotlib.pyplot as plt

x=[0,1,0.5,0]
y=[0,0,1,0]

plt.plot(x,y, marker="o", linestyle='-',color='c', label='Line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('48-Shekhar Suman \n Line plot')
plt.legend()
plt.show()
