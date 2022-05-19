# 3. Scrieti o functie care primeste doua liste ca parametri. Listele contin numere intregi.
# Fct. returneaza o singura lista formata din inmultirea dupa cum urmeaza: primul elem. din prima 
# lista X primul elem. din a 2-a lista .... etc.
# [1, 2, 3]
# [3, 4, 6]
# => [3, 8, 18]

list1 = [2,5,6]
list2 = [1,3,4]

products = []

for i in range(0, len(list1)):
    products.append(list1[i] * list2[i])

print(products)