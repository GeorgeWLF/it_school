user_info = {
    "name": "Alex Radu",
    "age": 28,
    "gender": "M",
    "email": "radu.alex@gmail.com"
}

# lista cheilor

# print(user_info.keys())

u_i_keys1 = list(user_info.keys())

for key in u_i_keys1:
    print(key)

user_info["address"] = "Bucharest"

print("-" * 30)

for key in u_i_keys1:
    print(key)

print("-" * 30)

if len(u_i_keys1) == len(user_info.keys()):
    print("Dictionar nemodificat")
else:
    print("Dictionar modificat")

