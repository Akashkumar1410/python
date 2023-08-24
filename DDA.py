import matplotlib.pyplot as plt


def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1

    x_points = []
    y_points = []

    for _ in range(int(steps) + 1):
        x_points.append(x)
        y_points.append(y)
        x += x_increment
        y += y_increment

    return x_points, y_points


# Get user input for the coordinates of the endpoints
x1 = float(input("Enter x-coordinate of the first endpoint: "))
y1 = float(input("Enter y-coordinate of the first endpoint: "))
x2 = float(input("Enter x-coordinate of the second endpoint: "))
y2 = float(input("Enter y-coordinate of the second endpoint: "))

# Calculate the points along the line using DDA
x_points, y_points = dda_line(x1, y1, x2, y2)

# Get user input for the pixel index
pixel_index = int(input("Enter the index of the pixel you want to compute: "))
if pixel_index < 0 or pixel_index >= len(x_points):
    print("Invalid pixel index!")
else:
    pixel_x = x_points[pixel_index]
    pixel_y = y_points[pixel_index]
    print(f"Pixel coordinates: ({pixel_x}, {pixel_y})")

    plt.plot(x_points, y_points, marker='o')
    plt.plot(pixel_x, pixel_y, marker='x', color='red', label='Selected Pixel')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('DDA Line Algorithm')
    plt.grid(True)
    plt.legend()
    plt.show()
