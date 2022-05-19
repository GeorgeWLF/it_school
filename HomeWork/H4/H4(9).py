# 9) Make a function for printing the first 5 longest strings in a list ; (len("test"))


list = ['Mihai', 'Alex', 'Catalin', 'George', 'Radu', 'Simona']

# print (max(list, key=len))
# list.remove(max(list, key=len))

# print (max(list, key=len))
# list.remove(max(list, key=len))

# print (max(list, key=len))
# list.remove(max(list, key=len))

# print (max(list, key=len))
# list.remove(max(list, key=len))

# print (max(list, key=len))
# list.remove(max(list, key=len))

for i in range(0, len(list)):
    if i <= 4:
         print (max(list, key=len))
         list.remove(max(list, key=len))