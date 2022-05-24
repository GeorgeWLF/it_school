empty_dict = {}
empty_dict1 = dict()

user_info = {
    "name": "Alex Radu",
    "age": 28,
    "gender": "M",
    "email": "radu.alex@gmail.com"
}

# user_info1 = ["Alex", 28, "alex.radu@gmail.com", "M"]

# print(empty_dict)
# print(type(empty_dict))

# accesare
print("Nume:", user_info["name"])
print("Varsta:", user_info["age"])

print(user_info.get("address", "Not find"))
print(user_info.get("name", "Not find"))

# modificare
print("-----------------------------------")

user_info["name"] = "George"
print("Nume:", user_info["name"])
print("Varsta:", user_info["age"])

# adaugare
print("-----------------------------------")

print(empty_dict)

empty_dict["ro"] = "Buna ziua!"

print(empty_dict)

empty_dict["en"] = "Good afternoon!"

print(empty_dict["en"])

# stergere
print("-----------------------------------")

del user_info["email"]
print(user_info)

# CRUD - create read update delete
print("-----------------------------------")

empty_dict1 = {
    2010: "Dragon",
    2011: "Cocos",
    2012: "Iepure"
}

# empty_dict1[2010] = "Dragon"
# empty_dict1[2011] = "Cocos"

empty_dict1[2013] = "Catel"

print(empty_dict1[2013])


fool = {
    2: "Two",
    # 2.0: "Almost two", ----> 2.0 este vazut ca si 2
    2.1: "Almost two"
}

print(fool[2])