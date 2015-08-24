__author__ = 'anhhoangta'
import time
import math

primeinLineCount = 0
primeCount = 0
time_start = time.clock()
i=2
while primeCount < 100:
    for j in range(2,int(math.sqrt(i))+1):
        if i%j == 0:
            break
    else:
        print("{0:5d}" .format(i), end="")
        primeCount += 1
        primeinLineCount += 1
        if primeinLineCount > 9:
            print("")
            primeinLineCount = 0
    i += 1

time_end = time.clock()
print()
print("Print first 100 primes number in: {0:5f} miliseconds" .format((time_end-time_start)*1000))
