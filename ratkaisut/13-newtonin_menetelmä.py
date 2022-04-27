def f(x):
    return x**3 - 3 * x + 1

# funktion f derivaatta
def d(x):
    return 3 * x**2 - 3

def n(x):
    return (x - f(x) / d(x))

x = 2 # alkuarvaus
# suorittaa menetelmän 10 kertaa
for i in range(1, 11):
    x = n(x)

print('funktion f(x) nollakohdan likiarvo: ', f(x))
