import matplotlib.pyplot as plt
import numpy as np 
def rotate_2d(points, angle_degrees, rotation_center=(0, 0)): 
    angle_radians = np.radians(angle_degrees)
    cos_theta = np.cos(angle_radians)
    sin_theta = np.sin(angle_radians)
    rotated_points = []
    for point in points:
        x, y = point
        x_centered = x - rotation_center[0]
        y_centered = y - rotation_center[1]
        rotated_x = x_centered * cos_theta - y_centered * sin_theta
        rotated_y = x_centered * sin_theta + y_centered * cos_theta
        rotated_x += rotation_center[0]
        rotated_y += rotation_center[1]
        rotated_points.append((rotated_x, rotated_y))
    return rotated_points
def plot_points(points, color='b', label=None): 
    x, y = zip(*points)
    plt.scatter(x, y, color=color, label=label)
original_points = [(1, 1), (2, 3), (3, 2), (4, 4)]
rotation_angle = 45
rotation_center = (2, 2)
rotated_points = rotate_2d(original_points, rotation_angle, rotation_center)
plot_points(original_points, color='b', label='Original Points')
plot_points(rotated_points, color='r', label=f'Rotated Points (Angle: {rotation_angle})')
plt.axis('equal')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('48 - SHEKHAR SUMAAN \n 2D ROTATION EXAMPLE')
plt.legend()
plt.grid(True)
plt.show()