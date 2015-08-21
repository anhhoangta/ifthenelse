__author__ = 'anhhoangta'
import time
import math

count = 0
time_start = time.clock()
for i in range (2,1000):
    for j in range(2,int(math.sqrt(i))+1):
        if i%j == 0:
            break
    else:
        print(i)
        count += 1
        if count >100:
            break
time_end = time.clock()
print("Print first 100 primes number in: {0:5f} miliseconds" .format((time_end-time_start)*1000))
