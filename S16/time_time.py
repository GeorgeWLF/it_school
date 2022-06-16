from datetime import datetime
import time

# timestamp - secunde trecute de la  01.01.1970 00:00:00 UTC
print(time.time())

b_day = time.strptime("04/23/1999", "%m/%d/%Y")

wday = {
    0: "Luni",
    1: "Marti",
    3: "Joi",
    4: "Vineri",
    5: "Sambata",
    6: "Duminica"
}

# print(wday[b_day.tm_wday])

b_day_ts = time.mktime(b_day)

print(time.strftime("%Y", b_day))

