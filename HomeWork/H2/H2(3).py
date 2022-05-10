# Scrieti un program care citeste de la tastatura un nr natural "n", 
# si afiseaza suma primelor n numere multiple de 5 si 3.

n = input("n = ")
n = int(n)

suma = 0

for i in range(3, n, 3):
    if i % 5 == 0:
        suma = suma + i
        print(suma)
