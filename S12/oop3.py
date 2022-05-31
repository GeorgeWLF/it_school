from auto import Car

ford = Car(4, "manual", False)

vw = Car(2, "auto", "False")

toyota = Car(4, "manual", True)

print("Start")
print(toyota.get_gas_level())

print("Alimentam 50 litri")
toyota.refill(50)

print(toyota.drive(100))

print("*" * 50)

print(toyota.drive(100))