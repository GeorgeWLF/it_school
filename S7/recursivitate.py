# 4! = 1 * 2 * 3 *4 *5


def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n


# 1. factorial(3) * 4  (1 * 2 * 3 * 4)
# 2. factorial(2) * 3  (1 * 2 * 3)
# 3. factorial(1) * 2  (1 * 2)
# 4. 1


# 


print(factorial(4))