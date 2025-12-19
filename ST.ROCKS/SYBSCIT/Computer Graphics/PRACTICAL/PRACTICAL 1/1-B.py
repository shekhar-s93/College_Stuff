import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=20, color='skyblue')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('48 - SHEKHAR SUMAAN \n Histogram Chart')
plt.show()
