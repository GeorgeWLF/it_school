from datetime import datetime

# b_day = datetime(1999, 4, 23)

# delta = datetime.now() - b_day

# print(delta)

t_year = datetime(2022, 1, 1)

delta = datetime.now() - t_year

print(delta.total_seconds() / 3600)