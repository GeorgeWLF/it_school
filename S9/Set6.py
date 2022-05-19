# scrieti un script care citeste de la tst 3 nr (a, b si c) si afiseaza toti multipli comuni intr-un interval.
# primul nr (a) reprezinta limita superioara a intervalului in care se opereaza, limita inferioara este 1
# celelalte 2 (b, c) sunt numerele pentru care se vor cauta multipli comuni

# extra: sa se verifice daca b si c sunt mai mari decat 1 si mai mici decat lim. sup. (a)
# daca nu sunt in intervalul respectiv sa se afiseze eroare

# a = 1000

# [2, 1000]
# b = 3
# c = 5

# # 15, 30, 45, 60.....

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

# for i in range(1, a):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

multiplii_b = list (range(1*b,a+1,b))
multimplii_c = list (range(1*c,a+1,c ))


set1 = set(multiplii_b)
set2 = set(multimplii_c)


intersec = set1.intersection (set2)
for i in intersec:
    print (i)