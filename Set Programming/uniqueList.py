fruits = ['Juice', 'Tomato', 'Potatoes', 'Banana', 'Tomato', 'Banana']

uniqueFruits = []
timeAppear = []

for fruit in fruits:

    if fruit not in uniqueFruits:
        uniqueFruits.append(fruit)
        timeAppear.append(fruits.count(fruit))

print(list(zip(uniqueFruits, timeAppear)))