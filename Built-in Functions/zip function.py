x = [9, 2, 3, 2, 1, 2, 1, 2, 13]
y = [4, 5, 6, 7, 12, 15, 8, 10]

result = []
for num_x, num_y in zip(x, y):
    if num_x + num_y <= 10:
        result.append(tuple([num_x, num_y]))
print(result)

"""
#another solution

for i in reversed(range(0, min(len(x), len(y)))):
    if x[i]+y[i] > 10:
        del x[i], y[i]
print(list(zip(x, y)))
"""