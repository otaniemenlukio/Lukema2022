print('ax^2 + bx + c = 0')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

d = b**2 - 4 * a * c

if d > 0:
    print('yhtälöllä on 2 ratkaisua')
elif d == 0:
    print('Yhtälöllä on 1 ratkaisu')
else:
    print('yhtälöllä ei ole ratkaisuja')
