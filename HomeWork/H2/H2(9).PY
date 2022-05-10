# 9. Sa se modifice programul de la pct. 8 astfel:
#     - modificam intervalul de generare la [1, 300]
#     - in loc de + - o sa afisam dupa cum urmeaza;
#     - cand numarul introdus este:
#         +/- 50 fata de numarul cautat: "Gheata"
#         +/- 40 fata de numarul cautat: "Frig"
#         +/- 30 fata de numarul cautat: "Rece"
#         +/- 20 fata de numarul cautat: "Caldut"
#         +/- 10 fata de numarul cautat: "Cald"
#         +/- 5 fata de numarul cautat: "Frige"
#         +/- 2 fata de numarul cautat: "Arde"

#     EX:
#     Incepe jocul!
#     Introduceti un numar intre 1 si 99.
#     50
#     Caldut
#     44
#     Caldut
#     60
#     Rece
#     34
#     Frige
#     33
#     Frige
#     31
#     Arde
#     Felicitari!
#     Ai ghicit numarul: 31

import random
import math

print("Incepe jocul!")
print("Introduceti un numar intre 1 si 99")

n = -1
x = random.randint(1, 100)

while x != n:
    
    n = int(input(" "))

    if x > n:
        if x-n <= 50:
            print("Gheata")
        if x-n <= 40:
            print("Frig")
        if x-n <= 30:
            print("Rece")
        if x-n <= 20:
            print("Caldut")
        if x-n <= 10:
            print("Cald")
        if x-n <= 5:
            print("Frige")
        if x-n <= 2:
            print("Arde")
# daca pun if si urmand dupa doar elif imi va printa doar gheata
    else:
        if n-x <= 50:
            print("Gheata")
        if n-x <= 40:
            print("Frig")
        if n-x <= 30:
            print("Rece")
        if n-x <= 20:
            print("Caldut")
        if n-x <= 10:
            print("Cald")
        if n-x <= 5:
            print("Frige")
        if n-x <= 2:
            print("Arde")

print("Felicitari!")
print("Ai ghicit numarul:", n)
# daca inlocuiesc elif x < n cu else nu imi va mai printa cand x < n
#daca n-x < 2 imi va printa Gheata, Frig, Rece, Caldut, Frige, Arde in loc a printa doar Arde
#daca n-x < 20 imi va printa Gheata, Frig, Rece, Caldut