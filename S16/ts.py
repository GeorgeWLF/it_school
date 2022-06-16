import time

some_ts = 1655225169.3462327

ts_struct = time.gmtime(some_ts)

print(ts_struct.tm_hour)
print(ts_struct.tm_min)

print(time.strftime("%m/%d/%Y", ts_struct))