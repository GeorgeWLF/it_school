user_info = {
    "name": "Alex Radu",
    "age": 28,
    "gender": "M",
    "email": "radu.alex@gmail.com"
}

# lista valorilor; values => obiect de tip view

# for v in user_info.values():
#     print(v)

u_i_values1 = user_info.values()

print(type(u_i_values1))

for v in u_i_values1:
    print(v)