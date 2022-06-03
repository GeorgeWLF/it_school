from auto import Car

ford = Car(False)

vw = Car(True, 2)

toyota = Car(False, 2 , True)

print("Start")
print(toyota.get_gas_level())

print("Alimentam 50 litri")
toyota.refill(50)

# print(toyota.drive(100))

# print("*" * 50)

# print(toyota.drive(100))