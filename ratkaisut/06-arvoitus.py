tulo = 47804
for c in range(int(tulo**(1/3)) + 1, 0, -1):
    b = c + 3
    a = b + 1
    if a * b * c == tulo:
        print('Aatami:', a, '\nBertta:', b, '\nCecilia:', c)
        break
