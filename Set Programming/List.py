def filterDup(list):
    for item in list:
        while list.count(item) > 1:
            del list[list.index(item)]
    return list

print(filterDup(["tom", "jerry", "dog", "tom"]))