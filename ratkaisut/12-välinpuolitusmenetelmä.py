from math import sin

def f(x):
    return sin(x) - x + 1

yläraja = 2
alaraja = 1

while abs(yläraja - alaraja) > 1e-3:
    # muuttujaa vastaus voi käyttää silmukan jälkeen
    vastaus = (alaraja + yläraja) / 2
    if f(alaraja) * f(vastaus) < 0:
        yläraja = vastaus
    else:
        alaraja = vastaus

print(f"nollakohdan likiarvo tuhannesosan tarkkuudella on {vastaus}")
