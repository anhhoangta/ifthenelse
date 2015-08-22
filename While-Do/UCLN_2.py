import  time

while True:

    a = int (input("Please enter first integer: "))
    b = int (input("Please enter second integer: "))
    time_start = time.clock()

    gcd = 1
    k=2

    while k <= a and k <= b:
        if a%k == 0  and b%k == 0:
            gcd = k
        k+=1
    print("Greatest common divisor is: %d" %gcd)
    time_end = time.clock()
    print("Completed in: {0:5f} miliseconds" .format((time_end-time_start)*1000))