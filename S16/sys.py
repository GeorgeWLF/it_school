from datetime import datetime
import sys

user_choice = int(input("Enter a number:"))

if user_choice % 2 == 0:
    print("Numarul este par")
    print("Program terminat cu sys")
    sys.exit
else:
    print("Numarul este impar")
    print("Programul continua")

print(datetime.now())