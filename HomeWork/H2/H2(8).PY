# 8. Scrieti un program de tip joc "ghiceste numarul".
#     Cerinte: 
#     1. Programul genereaza un numar aleator in intervalul [1, 99].
#     2. Intr-o bucla conditionata de gasirea numarului cautat:
#         - se citeste de la tastatura un numar
#         - se compara cu numarul cautat
#         - daca numarul introdus este mai mic decat numarul cautat se afiseaza +
#         - daca este mai mic se afiseaza -
#     3. Dupa ce numarul este ghicit se afiseaza un mesaj de felicitare si numarul cautat.

#     EX: 
#     Incepe jocul!
#     Introduceti un numar intre 1 si 99.
#     3
#     +
#     6
#     +
#     20
#     +
#     60
#     -
#     50
#     +
#     56
#     -
#     Felicitari!
#     Ai ghicit numarul: 56
import random

print("Incepe jocul!")
print("Introduceti un numar intre 1 si 99")

n = -1
x = random.randint(1, 100)

while x != n:
    
    n = int(input(" "))
    
    if x > n:
        print(" + ")


    else:
        print(" - ")


print("Felicitari!")
print("Ai ghicit numarul: ", n)
        
        #nu printeaza print("Felicitari!")
        # print("Ai ghicit numarul:", n)
        
