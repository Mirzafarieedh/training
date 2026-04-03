def numerical_derivative(f, x, h=0.001):
    return (f(x + h) - f(x)) / h

def f(x):
    return x**2

# Takes list of (x,y) pairs, finds max slope between consecutive points
points = [(-3, 9), (-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4), (3, 9)]

print("Slopes between consecutive points:")
max_slope = 0
max_pair = None

for i in range(len(points) - 1):
    x1, y1 = points[i]
    x2, y2 = points[i+1]
    slope = (y2 - y1) / (x2 - x1)
    print(f"  ({x1},{y1}) → ({x2},{y2}) | slope = {slope:.4f}")
    if abs(slope) > abs(max_slope):
        max_slope = slope
        max_pair = (points[i], points[i+1])

print(f"\nMax slope: {max_slope} between {max_pair}")