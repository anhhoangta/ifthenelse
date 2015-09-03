while True:
    oddnum = int(input("Please input an odd integer: "))
    listNumber =[]
    if oddnum % 2 == 0:
        print("Sorry, the number you entered is an even number")
    else:
        for i in reversed(range(1, oddnum+1)):
            if i % 2 != 0:
                listNumber = [i]*i
                print(str(''.join(map(str, listNumber))).center(oddnum*len(str(oddnum))))
        print()