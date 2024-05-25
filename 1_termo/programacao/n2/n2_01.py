from random import randint
a = []
b = []
for i in range(20):
    a.append(randint(1, 50))
    if a[i] % 2 == 0:
        b.append(a[i])
    else:
        b.append(a[i] * 2)
print(f"Vetor antes da alteração -> {a}")
print(f"Vetor ápos alteração -----> {b}")