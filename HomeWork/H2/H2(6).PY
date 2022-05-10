# Intr-o cutie se află 300 de bile, numerotate cu numere începând de la unu, 
# din trei în trei. Toate bilele cărora le corespund numere pare sunt verzi. 
# Să se afle câte bile verzi sunt.


# V1
# c=0

# for i in range(1, 900, 3):
#     if i % 2 == 0:
#         c = c + 1

# print("Bile verzi = ", c)

i = 0
nr_pe_bile = 1
bile_verzi = 0

while i <= 300 :
    if nr_pe_bile % 2 == 0 :
        bile_verzi += 1
    i += 1
    nr_pe_bile += 3 
print ("Bile verzi= ",bile_verzi)