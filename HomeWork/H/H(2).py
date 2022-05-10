r = input("raza =")
r = int(r)

import math

perimetrul = 2 * math.pi * r
aria = math.pi * r ** 2

#perimetrul cercului = 2 * pi * r
#aria cercului = pi * r ** 2

if (r <= 100):
    print ("Perimetrul cercului =" , perimetrul )

else:
    print ("Aria cercului =" , aria )