# 4) Create a mixed (sting and int) list with 10 elements
# 5) Print first and last element
# 6) Replace second element with 144
# 7) Print the index of element with value 144


list = [1, 5, "Mihai", 6, 35, "Radu", 115, "Catalin", 322, "Zar"]

print("Original list: ", list)

print("First element: ", list[0])
print("Last element: ", list[-1])

list[1] = 144
print("List after replacing second element:", list)

print("Index of element with value 144 is: ", list.index(144))