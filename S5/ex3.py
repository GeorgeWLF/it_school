# 3. Scrieti o functie care returneaza daca unu nr. (reprezentan un an) este
# considerat an bisect.

# def is_bisect(n):
#     """Check if the year is bisect."""
#     if n % 4 == 0:
#         return True
#     else:
#         return False

# if is_bisect(2000):
#     print("Este bisect")
# else:
#     print("Nu este bisect")


#VARIANTA 1

# year = int(input("Introdu un an: "))

# def is_bisect(n):
#      if n % 400 == 0:
#          return True
#      elif n % 100 == 0:
#                return False
#      else:
#           if n % 4 == 0:
#                return True
          

# if is_bisect(year):
#     print("este bisect")
# else:
#     print("nu este bisect")


# VARIANTA 2

# year = int(input("Introdu un an: "))

# def is_bisect(n):
#      if n % 400 == 0 and n % 100 == 0:
#          return True

#      else:
#           if n % 4 == 0 and n % 100 != 0:
#                return True
          

# if is_bisect(year):
#     print("este bisect")
# else:
#     print("nu este bisect")


