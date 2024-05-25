from random import randint
a = []
for i in range(15):
    a.append(randint(1, 40))
print(f"Lista de números -> {a}")
for i in range(15):
    for j in range(i+1, 15):
        if a[j] < a[i]:
            a[i], a[j] = a[j], a[i]
print(f"Segundo maior valor é -> {a[i-1]}")