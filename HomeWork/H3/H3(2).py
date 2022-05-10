# 4. Scrieti o functie care returneaza volumul unui cub in litri. Aceasta va primi
# un singur agument reprezentand muchia cubului in metri.

# 5. Scrieti o functie care returneaza volumul unui cilintru in litri,
# Aceasta va primi doua argumente reprezentand inaltimea si raza bazei in metri.

# 6. Scrie o functie care converteste litrii in metri cubi.

# 7. Foloseste functiile de la pct. 4-6 pentru a calcula cate cuburi cu muchia de 18 metri
# sunt necesare pentru a umple un cilindru cu raza bazei de 20 m si inaltimea de 55 m.
# - Printeaza volumul cubului in metri cubi #### Volumul cubului: 20 m^3
# - Printeaza volumul cilindrului in metri cubi.
# - Printeaza rezultatul de la pct. 7
# - Toate valorile printate vor fi insotite de mesaje descriptive.
import math

# Exercitiul 4
def cube_volume_in_liters(e):
    # edge = int(input("Edge: "))
    # return edge ** 3 * 1000
    return e ** 3 * 1000
    

# volumul_unui_cub_in_litri()

# Exercitiul 5

def cylinder_volume_in_liters(r, h):
    # inaltimea = int(input("Inaltimea: "))
    # raza = int(input("Raza: "))
    # return (3.14 * raza**2) * inaltimea
    return ((3.14 * r**2) * h) * 1000
    # print("Volumul unui cilindru:", n, "Litri")

# volumul_unui_cilindru_in_litri()

# Exercitiul 6

# litri = int(input("Litri: "))

def convert_to_m3(liters):
    # liters = int(input("Liters: "))
    return liters / 1000
    
# Exercitiul 7

print("Cube volume: ", convert_to_m3(cube_volume_in_liters(18)) ,"m3")
print("Cylinder volume", convert_to_m3(cylinder_volume_in_liters(20, 55)), "m3")
print("Cubes in cylinder = ", convert_to_m3(cylinder_volume_in_liters(55, 20)) // convert_to_m3(cube_volume_in_liters(18)), "Cubes")