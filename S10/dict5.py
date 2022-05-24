user_info = {
    "name": "Alex Radu",
    "age": 28,
    "gender": "M",
    "email": "radu.alex@gmail.com"
}

china_years = {
    2010: "Dragonului",
    2011: "Cocosului",
    2012: "Iepurelului"
}

# sortare dupa chei

sorted_user_info = sorted(user_info.items())
sorted_user_info_reverse = sorted(user_info.items(), reverse=True)

for k, v in sorted_user_info:
    print(k,"||", v)

# sortare dupa valori
print("-" * 30)

def comparator(t):
    return t[1]

for k, v in sorted(china_years.items(), key=lambda x: x[1]):
    print("Anul", k, " a fost in", v)
