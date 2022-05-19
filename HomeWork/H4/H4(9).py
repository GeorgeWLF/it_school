# 9) Make a function for printing the first 5 longest strings in a list ; (len("test"))

# Var1

# list = ['Mihai', 'Alex', 'Catalin', 'George', 'Radu', 'Simona']

# # for i in range(0, len(list)):
# #     if i <= 4:
# #          print (max(list, key=len))
# #          list.remove(max(list, key=len))

# Var2

cfr = ["petrescu", "omrani", "debeljiuc", "boateng", "deac" , "petrila", "grahovac"]

def len_is (string):
    print("Key function called with: ", string)
    return len(string)

def longest_strings (lst) :
    lst.sort(key=len_is, reverse=True)
    print (lst[:5])

longest_strings (cfr)