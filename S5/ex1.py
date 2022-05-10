def is_even(n):
    """Check if number is even."""

    if n % 2 == 0:
        return True
    else:
        return False

# print(is_even(10))

# for i in range(101):
#     print(is_even(i))

# for i in range(101):
#     if is_even(i):
#         print("**")
#     else:
#         print("--")

for i in range(10):
    if is_even(i):
        print(i, "este par")
    else:
        print(i, "este impar")