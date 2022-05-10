# 2. Utilizati functia de la pct 1 pentru a afisa toate numerele impare in intervalul
# [0, 50] si in intervalul [2000, 2100].

def impare(n):
    if n % 2 == 0:
        return True
    else:
        return False 

for i in range(0,50):
    if not impare(i):
        print(i, end= " ")

for i in range(2000, 2101):
    if not impare(i):
        print(i, end = " ")