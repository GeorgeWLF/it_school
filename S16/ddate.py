# from datetime import date, time
# print(date.today())

from datetime import datetime


# formatare ora
print(datetime.now().strftime("%H: %M: %S"))

# formatare data
print(datetime.now().strftime("%d/%B/%y"))  # 14/Jun/22

# 8/29/1993

b_day = datetime(1999, 4, 23)

print(b_day.strftime("%m/%d/%Y"))