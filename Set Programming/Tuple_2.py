numList = [9, 3, 2, 5, 6, 8, 11]
listLessOrEqual5 = []
listGreatThan5 = []
Result = ()

def sort(list):
    for i in range(0, len(list)-1):
        for j in range(i+1, len(list)):
            if list[i] >= list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

for num in numList:
    if num <= 5:
        listLessOrEqual5.append(num)
    else:
        listGreatThan5.append(num)
Result = (sort(listLessOrEqual5), sort(listGreatThan5))
print(Result)
