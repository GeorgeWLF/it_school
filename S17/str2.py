list1 = ['a', 'b', 'c']
# vrem sa obtinem a>b>c
# sau a_b_c

# join

new_str = ">".join(list1)
new_str2 = "_".join(list1)
new_str3 = ", ".join(list1)
new_str4 = "\\".join(list1) # using only 1 \ will give error

# print(new_str)

# \ = escape character

# c-b-a
new_str5 = "-".join(reversed(list1))

