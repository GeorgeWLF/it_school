# 1. Definiti o matrice 5 x 5 si afisati numerele de pe diagonala principala si numerele de pe diagonala secundara.

# 1 2 3
# 4 5 6
# 7 8 9

# Diag principala 1 5 6
# Diag secundara 3 5 7


m = [[5, 10, 8, 3, 6],
    [6, 2, 7, 6, 10],
    [10, 2, 11, 52, 6],
    [22, 9, 10, 17, 4],
    [2, 1, 33, 45, 66]]

print("Diag principala:" ,m[0][0], m[1][1], m[2][2], m[3][3], m[4][4])

print("Diag secundara:" ,m[0][4], m[1][3], m[2][2], m[3][1], m[4][0])