import matplotlib.pyplot as plt

sizes = [25, 30, 15, 20, 10]
labels = ['A', 'B', 'C', 'D', 'E']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['red', 'green', 'blue', 'yellow', 'purple'])                                                         

plt.axis('equal')
plt.title('48 - SHEKHAR SUMAN \n Pie Chart')
plt.show()
