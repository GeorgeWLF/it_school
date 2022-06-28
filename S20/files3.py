try:
    f_out = open("ouput.txt", "w")
except OSError as err:
    print("Nu pot deschide fisierul.")

for i in range(100):
    f_out.write(f"No: {i}\n")

f_out.close()