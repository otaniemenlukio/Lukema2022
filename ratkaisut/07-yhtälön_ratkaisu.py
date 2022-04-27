def f(x):
    return 2 * x**3 - 172 * x**2 - 288 * x + 199808

x = 0
while f(x) != 0:
    print(x, f(x))
    x += 1

print(x, f(x))
