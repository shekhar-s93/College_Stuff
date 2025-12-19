import matplotlib.pyplot as plt

def midpoint_ellipse(a, b):
    x, y = 0, b
    a_sqr = a**2
    b_sqr = b**2

    d1 = (b_sqr - (a_sqr * b) + 0.25 * a_sqr)
    dx = 2 * b_sqr * x
    dy = 2 * a_sqr * y

    x_points = []
    y_points = []

    plot_ellipse_points(x, y, x_points, y_points)

    while dx < dy:
        x += 1
        dx += 2 * b_sqr
        if d1 < 0:
            d1 += dx + b_sqr
        else:
            y -= 1
            dy -= 2 * a_sqr
            d1 += dx - dy + b_sqr
        plot_ellipse_points(x, y, x_points, y_points)

    d2 = b_sqr * (x + 0.5)*2 + a_sqr * (y - 1)*2 - a_sqr * b_sqr
    while y > 0:
        y -= 1
        dy -= 2 * a_sqr
        if d2 > 0:
            d2 += a_sqr - dy
        else:
            x += 1
            dx += 2 * b_sqr
            d2 += a_sqr + dx - dy
        plot_ellipse_points(x, y, x_points, y_points)

    return x_points, y_points

def plot_ellipse_points(x, y, x_points, y_points):

    x_points.extend([x, -x, x, -x])
    y_points.extend([y, y, -y, -y])


a, b = 5, 3

x_points, y_points = midpoint_ellipse(a, b)

plt.scatter(x_points, y_points, marker='.', color='b')
plt.title("48 - Shekhar Suman \n Midpoint Ellipse Drawing Algorithm")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.axis('equal')
plt.grid(True)
plt.show()
