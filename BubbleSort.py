__author__ = 'anhhoangta'
import  random
import string

nameList = []
for num in range (10):
    nameList.append("".join(random.sample(string.ascii_lowercase+" ",random.randint(5,10))))

for idx in range(len(nameList)):
    if nameList[idx].find(" ") < 2 or nameList[idx].find(" ")>=4:
        if len(nameList[idx])>=6:
            nameList[idx] = nameList[idx].replace(" ","")
            ran = random.randint(3,4)
            nameList[idx] = nameList[idx][:ran]+ " " +nameList[idx][ran:]
        if len(nameList[idx])<6:
            nameList[idx] = nameList[idx].replace(" ","")
            if nameList[idx].find(" ")>=2:
                nameList[idx] = nameList[idx].replace(" ","")
print(nameList)

for i in range(0, len(nameList)-1):
    for j in range(i+1, len(nameList)):
        if nameList[i][0] <= nameList[j][0]:
            temp = nameList[i]
            nameList[i] = nameList[j]
            nameList[j] = temp
print(nameList)

"""
for i in range(0, len(nameList)-1):
    for j in range(i+1, len(nameList)):
        if ord(nameList[i][0])<=ord(nameList[j][0]):
            temp = nameList[i]
            nameList[i] = nameList[j]
            nameList[j] = temp
print(nameList)
"""