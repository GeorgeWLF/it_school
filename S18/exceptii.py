from math import pi

def circle_area(radius):
    return pi * radius ** 2

def cylinder_volume(radius, height):
    return circle_area(radius) * height

# height = int(input("Inaltimea: "))
# radius = int(input("Raza: "))
# print(f"Volum cilindru: {cylinder_volume(radius, height)}")

# circle_area(None)
# circle_area("@#!#$")
# circle_area(0)
# circle_area(2.3)
# circle_area({})
# circle_area([])
# circle_area(())
# circle_area(print)

# print("########")