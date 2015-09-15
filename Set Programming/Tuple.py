l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e']
print(list(zip(l1, l2[::-1])))
#print(list(zip(l1, list(reversed(l2)))))