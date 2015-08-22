while True:
    numberString = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín", "mười", "trăm", "nghìn",
                    "triệu", "tỉ"]
    numberSubString = ["mươi", "lăm", "mốt", "lẻ"]

    Bool = True
    while Bool:
        number = input("Please input number: ")
        if number.isnumeric() == False:
            if (number.replace(",","").isnumeric() == True and number.count(",") ==1) or \
                (number.replace(".","").isnumeric() == True and number.count(".") ==1) or \
                    (number.replace("/","").isnumeric() == True and number.find("/")>0 and number.count("/") == 1):
                Bool = False
            else:
                Bool = True
        elif number[0] == "0":
            number = number.replace("0", "")
            Bool = False
        elif int(number) == 0:
            number = 0
        else:
            Bool = False


    def toString2(index, str2):
        result = ""

        if str2[0] == "0":
            if str2[1] == "0":
                result = numberString[11]
            else:
                result = numberSubString[3] + " " + numberString[int(str2[1])]

        elif str2[0] == "1":
            if str2[1] == "5":
                result = numberString[10] + " " + numberSubString[1]

            elif str2[1] == "0":
                result = numberString[10]

            else:
                result = numberString[10] + " " + numberString[int(str2[1])]

        elif str2[1] == '0':
            result = numberString[int(str2[0])] + " " + numberSubString[0]

        elif str2[1] == '1':
            result = numberString[int(str2[0])] + " " + numberSubString[0] + " " + numberSubString[2]

        elif str2[1] == '5':
            result = numberString[int(str2[0])] + " " + numberSubString[0] + " " + numberSubString[1]

        else:
            result = numberString[int(str2[0])] + " " + numberSubString[0] + " " + numberString[int(str2[1])]

        return result


    def toString(index, str):
        result = ""
        if index == 1:
            result = numberString[int(str)]

        if index == 2:
            result = toString2(2, str)

        if index == 3:
            if str[1] == "0" and str[2] == "0":
                if str[0] == 0:
                    result = numberString[12]
                else:
                    result = numberString[int(str[0])] + " " + toString2(2, str[1:])
            else:
                result = numberString[int(str[0])] + " " + numberString[11] + " " + toString2(2, str[1:])

        return result


    def toResult(inputNumber):
        result = ""
        if len(inputNumber) / 3 <= 1:
            result = toString(index=len(inputNumber), str=inputNumber)

        if len(inputNumber) / 3 <= 2 and len(inputNumber) / 3 > 1:
            if int(inputNumber[len(inputNumber) - 3:]) == 0:
                result = toString(len(inputNumber) - 3, inputNumber[:len(inputNumber) - 3]) + " " + numberString[12]
            else:
                result = toString(index=len(inputNumber) - 3, str=inputNumber[:(len(inputNumber) - 3)]) + " " + \
                         numberString[12] + " " + toString(
                    index=3, str=inputNumber[len(inputNumber) - 3:])

        if len(inputNumber) / 3 <= 3 and len(inputNumber) / 3 > 2:
            if int(inputNumber[len(inputNumber) - 5]) == 0:
                if int(inputNumber[len(inputNumber) - 6:]) == 0:
                    result = toString(len(inputNumber) - 6, inputNumber[:len(inputNumber) - 6]) + " " + numberString[13]
                else:
                    result = toString(len(inputNumber) - 6, inputNumber[:len(inputNumber) - 6]) + " " + numberString[
                        13] + " " + toString(3, inputNumber[len(inputNumber) - 6:len(inputNumber) - 3]) + " "
                + numberString[12]

            else:
                result = toString(index=len(inputNumber) - 6, str=inputNumber[:(len(inputNumber) - 6)]) + " " + \
                         numberString[13] + " " + toString(
                    index=3, str=inputNumber[(len(inputNumber) - 6):(len(inputNumber) - 3)]) + " " + numberString[
                             12] + " " + toString(index=3, str=inputNumber[len(inputNumber) - 3:])

        if len(inputNumber) / 3 <= 4 and len(inputNumber) / 3 > 3:
            if int(inputNumber[len(inputNumber) - 8]) == 0:
                if int(inputNumber[len(inputNumber) - 9:]) == 0:
                    result = toString(len(inputNumber) - 9, inputNumber[:len(inputNumber) - 9]) + " " + numberString[14]
                else:
                    result = toString(len(inputNumber) - 9, inputNumber[:len(inputNumber) - 9]) + " " + numberString[
                        14] + " " + toString(3, inputNumber[len(inputNumber) - 9:len(inputNumber) - 6]) + " "
                    + numberString[13]
            else:
                result = toString(index=len(inputNumber) - 9, str=inputNumber[:(len(inputNumber) - 9)]) + " " + \
                         numberString[14] + " " + toString(
                    index=3, str=inputNumber[(len(inputNumber) - 9):(len(inputNumber) - 6)]) + " " + numberString[
                             13] + " " + toString(
                    index=3, str=inputNumber[(len(inputNumber) - 6):(len(inputNumber) - 3)]) + " " + numberString[
                             12] + " " + toString(
                    index=3, str=inputNumber[len(inputNumber) - 3:])
        return result

    if number.count(",") == 1:
        print(toResult((number[0:number.find(",")]))+" "+"phẩy"+" "+toResult((number[number.find(",")+1:])))

    elif number.count(".") == 1:
        print(toResult((number[0:number.find(".")]))+" "+"phẩy"+" "+toResult((number[number.find(".")+1:])))

    elif number.count("/") == 1:
        print(toResult((number[0:number.find("/")]))+" "+"phần"+" "+toResult((number[number.find("/")+1:])))

    elif len(number) <= 12:
        print(toResult(number))

    else:
        print(toResult(number[:len(number) - 9]) + " " + numberString[14] + " " + toResult(number[len(number) - 9:]))
