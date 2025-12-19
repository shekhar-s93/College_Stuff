import matplotlib.pyplot as plt 
def scale_2d(points, scale_factor): 
    scaled_points = [] 
    for point in points: 
        x, y = point
        scaled_x = x * scale_factor
        scaled_y = y * scale_factor
        scaled_points.append((scaled_x, scaled_y))
    return scaled_points
def plot_points(points, color='b', label=None): 
    x, y = zip(*points)     
    plt.scatter(x, y, color=color, label=label)
original_points = [(1, 1), (2, 3), (3, 2), (4, 4)] 
scale_factor = 2 
scaled_points = scale_2d(original_points, scale_factor)
plot_points(original_points, color='b', label='Original Points')
plot_points(scaled_points, color='r', label=f'Scaled Points (Factor: {scale_factor})')
plt.axis('equal')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('48 - SHEKHAR SUMAN \n 2D SCALING EXAMPLE')
plt.legend()
plt.grid(True)
plt.show()