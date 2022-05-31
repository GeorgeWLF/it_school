from auto import Car


volvo = Car()  # aici se apeleaza constructorul automat
vw = Car()
# auto.horn()

# print("Nivel conbustibil:", auto.get_gas(), "%")

# print(auto.get_gas())

# accesare atribute
print("Volvo gas:", volvo.get_gas())
print("VW gas:", vw.get_gas())

volvo.refill_full()
vw.refill(20)
print("-" * 50)

print("Volvo gas:", volvo.get_gas())
print("VW gas:", vw.get_gas())

# auto.gas_per = 1000
# print(auto.gas_per)
