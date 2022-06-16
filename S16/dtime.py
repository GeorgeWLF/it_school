# ora si data curenta?
from datetime import datetime
from multiprocessing import cpu_count
current_dt = datetime.now()


# Ziua curenta
print(current_dt.day)

# Luna curenta
print(current_dt.month)

# Anul curent
print(current_dt.year)

# Ora curenta
print("Ora:", current_dt.hour)

# Minute si secunde
print("Minute:", current_dt.minute)
print("Secunde:", current_dt.second)