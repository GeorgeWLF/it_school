# Scrie un program care citeste de la tastatura un nr. natural
# si verfica daca acesta este palindrom. 111 121 292 2992 33533

# Functie care returneaza True daca un nr este palindrom.

# Citim de la tst un nr

# Apelam fct.

# rev = 1
# rev = 17
# rev = 178

def reverse(n):
    # n = int(input("introdu numarul: "))
    rev = 0
    while n != 0:
        c = n % 10 # rest
        n = n // 10 # cat
        rev = rev * 10 + c

    return rev


def palindrom():
    """Check if palindrom."""
    n = int(input("Introdu numarul: "))
    if reverse(n) == n:
        return True
    else:
        if reverse(n) != n:
            return False


if palindrom():
    print("Numarul este palindrom")
else:
    print("Numarul nu este palindrom")
# print(palindrom())