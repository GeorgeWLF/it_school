# *++  k = stelute, n - k plusuri
# **+
# ***
n = input("n = ")

n = int(n)

k = 1

while k <= n:
    print("*" * k, "+" * (n - k), sep= "")
    k = k + 1

print("DONE")