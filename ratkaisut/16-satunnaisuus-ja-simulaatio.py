from random import randint

# a-kohta

kruunat = 0
klaavat = 0
for _ in range(1000):
    if randint(1, 2) == 1:
        kruunat += 1
    else:
        klaavat += 1

print(f"kruunia tuli {kruunat}")
print(f"klaavoja tuli {klaavat}")

# b-kohta

silmälukulaskin = [0, 0, 0, 0, 0, 0]
for _ in range(1000):
    silmäluku = randint(1, 6)
    silmälukulaskin[silmäluku - 1] += 1

for silmäluku, määrä in enumerate(silmälukulaskin):
    print(f"silmäluku {silmäluku + 1} tuli {määrä} heitosta")
