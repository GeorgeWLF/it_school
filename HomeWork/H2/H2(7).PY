# Scrieti un program care citeste doua nr de la tastatura si calculeaza produsul
# lor. A nu se utiliza operatorul de inmultire.

n = input("Primul numar = ")
x = input("Al doilea numar = ")

n = int(n)
x = int(x)

p = 0

for i in range(1, n + 1):
    p = p + x

print("Produsul =", p)