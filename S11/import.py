import time

from time import time

# print(time())

# help si dir

start = time.time()

for i in range(1000):
    print(10 ** i)

stop = time.time()

print("starter at", start)
print("end at:", stop)
print("Duration:", stop - start)