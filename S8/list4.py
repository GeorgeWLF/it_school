user_id = [33, 455, 3, 32, 34, 12, 90, 32, 234]

# reversul listei !! opereaza pe lista
print("Lista in stare initiala")
print(user_id)

user_id.reverse()

print("Dupa reverse")
print(user_id)

print("-" * 30)

# list sliceing
# primele 3 elemente
top_three_users = user_id[:3]

print("user_id", user_id)
print("top_three_users", top_three_users)

print("-" * 30)

# ultimul element
last_element = user_id[-1:]
print(last_element)

print("-" * 30)

# interval
print(user_id[1:4])
# list copy