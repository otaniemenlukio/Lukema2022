# a
print('kymmenen ensimmäistä jäsentä:')
j = [7]
for i in range(10):
    print(j[i], end=' ')
    j.append(j[-1] + 5)

# b
print('\n\n10 ensimmäisen jäsenen summa:', sum(j))

# c
j = [7]
while sum(j) < 1000:
    j.append(j[-1] + 5)

print('\non laskettava yhteen', len(j), 'jäsentä, että summa ylittää arvon 1000')
