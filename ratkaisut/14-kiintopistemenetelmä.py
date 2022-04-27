from math import sqrt

def g(x):
    return sqrt(x + 4)

x = 0
while abs(x - g(x)) > 1e-6:
    x = g(x)

print(f"x on noin {x:.6f}")
