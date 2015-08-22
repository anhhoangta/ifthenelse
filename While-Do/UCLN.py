import  time

while True:

    a = int (input("Please enter first integer: "))
    b = int (input("Please enter second integer: "))
    time_start = time.clock()
    if a < b:
        temp =a
        a = b
        b = temp

    while True:
        if a%b==0:
            print("Greatest common divisor is: %d" %b)
            break
        else:
            r = a%b
            a = b
            b = r
    time_end = time.clock()
    print("Completed in: {0:5f} miliseconds" .format((time_end-time_start)*1000))