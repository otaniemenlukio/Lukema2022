n = 500
seula = [0]*(n+1)
for i in range(2,n+1):
    for j in range(2*i,n+1,i):
        seula[j] = 1

summa = 0
for i in range(2,n+1):
    if seula[i] == 0:
        print(i)
        summa += i

print('ensimmäisten', n, 'alkuluvun summa on', summa)
