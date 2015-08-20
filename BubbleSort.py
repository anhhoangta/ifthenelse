__author__ = 'anhhoangta'
import  random
import string

#create a random list with chars
charList = []
for index in range (random.randint(5,10)):  #limit amount of chars in list from 5-10 random chars a-->z
    charList.append(random.choice(string.ascii_lowercase))  #append into charList
print(charList)

#convert all chars in charList to Ascii number
numberList =[]
for char in charList:
    numberList.append(ord(char))

#sort above numberList by Bubble Sort method
for i in range(0, len(numberList)-1):
    for j in range(i+1, len(numberList)):
        if numberList[i]>=numberList[j]:
            temp = numberList[i]
            numberList[i] = numberList[j]
            numberList[j] = temp

#reverse numberList after sorting
numberList.reverse()

#convert again from Ascii numbers to chars with upper letter from Z-->A
reverseCharList = []
for number in numberList:
    reverseCharList.append(chr(number).upper())
print(reverseCharList)
