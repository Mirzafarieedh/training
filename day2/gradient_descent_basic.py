import time

def f(x):
    return x**2

def derivative(f, x, h=0.001):
    return (f(x + h) - f(x)) / h

def gradient_descent(start_x, lr=0.1, steps=50):
    x = start_x

    for i in range(steps):
        grad = derivative(f, x)
        x = x - lr * grad

        print(f"Step {i}: x = {round(x,4)}, f(x) = {round(f(x),4)}")

    return x

# Run
gradient_descent(start_x=5)