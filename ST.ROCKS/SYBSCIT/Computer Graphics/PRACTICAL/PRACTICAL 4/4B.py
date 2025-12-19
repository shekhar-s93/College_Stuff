import matplotlib.pyplot as plt 

def bresenham_line(x1, y1, x2, y2): 
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    x, y = x1, y1
    error = dx - dy
    x_points = [x]
    y_points = [y]
    while x != x2 or y != y2: 
        x_points.append(x)
        y_points.append(y)
        error2 = 2 * error
        if error2 > -dy: 
            error -= dy
            x += sx
        if error2 < dx: 
            error += dx
            y += sy
    return x_points, y_points 
x1, y1 = 2, 2
x2, y2 = 8, 5
x_points, y_points = bresenham_line(x1, y1, x2, y2)
plt.plot(x_points, y_points, marker='o', linestyle='-', color='b') 
plt.title("48 - SHEKHAR SUMAN \n Bresenham's Line Drawing Algorithm") 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
plt.grid(True) 
plt.show()
