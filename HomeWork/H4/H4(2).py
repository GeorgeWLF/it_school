# 2. Scrieti o functie care returneaza True daca lista primita ca param. este sortata,
# altfel returneaza False.

list = ['Alex', 'Zogdan', 'Mihai']

print("Original list: ", list)

if (list == sorted(list)):
    print("True, List is sorted")
else:
    print("False, List is not sorted")
