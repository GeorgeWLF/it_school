# 8) Make a function to remove all the elements with a maximal value from a list; return a new list (original list does not modify)

list = [2, 6 ,8 ,25 ,4 ,33 , 545, 1,]

# print("Original list: ", list)

# list.remove(max(list))

# print ("List after first remove: ", list)

# list.remove(max(list))

# print ("List after second remove: ", list)

# list.remove(max(list))

# print ("List after third remove: ", list)

# list.remove(max(list))

# print ("List after fourth remove: ", list)

# list.remove(max(list))

# print ("List after fifth remove: ", list)

# list.remove(max(list))

# print ("List after sixth remove: ", list)

# list.remove(max(list))

# print ("List after seventh remove: ", list)

for i in range(0, len(list)):
    if i >= 1:
        list.remove(max(list))
        print ("List after each remove: ", list)