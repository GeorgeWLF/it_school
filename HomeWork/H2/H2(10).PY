# 10. Scrieti un program care citeste un numar natural (n) de la tastatura si 
# genereaza un grafic de forma:

# *
# *
# **
# ***
# *****
# ********

# Graficul va fi format din n linii iar pe fiecare linie se afiseaza x stelute.
# x reprezinta al n nr a lui Fibonacci.

n = input("n = ")
n = int(n)

k_1 = 0
k_2 = 1

count  = 0

while count < n:
    print("*" * k_1)
    
    f = k_1 + k_2
    k_1 = k_2
    k_2 = f
    
    count += 1
#k_1 si k_2 sunt primele 2 numere din sirul de nr a lui Fibonacci
#sirul lui Fibonacci este suma a doua nr Fibonacci anterioare
