import matplotlib.pyplot as plt 
def dda_line(x1, y1, x2, y2): 
    dx = x2 - x1
    dy = y2 - y1 
    steps = max(abs(dx), abs(dy)) 
    x_increment = dx / steps 
    y_increment = dy / steps 
    x, y = x1, y1 
    x_points = [x] 
    y_points = [y] 
    for _ in range(steps): 
        x += x_increment         
        y += y_increment 
        x_rounded = round(x)         
        y_rounded = round(y) 
        x_points.append(x_rounded)         
        y_points.append(y_rounded) 
    return x_points, y_points 
x1, y1 = 2, 2  
x2, y2 = 8, 5 
x_points, y_points = dda_line(x1, y1, x2, y2) 
plt.plot(x_points, y_points, marker='o', linestyle='-', color='b') 
plt.title('48 - SHEKHAR SUMAN \n  DDA Line Drawing Algorithm') 
plt.xlabel('X-axis') 
plt.ylabel('Y-axis') 
plt.grid(True) 
plt.show()
