__author__ = 'anhhoangta'

inputweight = input("Enter your weight (pounds): ")
inputheight = input("Enter your weight (inches): ")

if inputweight.isnumeric() and inputheight.isnumeric():

    weightinkilogram = float (inputweight) * 0.45359237
    heightinmeter = float (inputheight) * 0.0254
    BMIindex = weightinkilogram / (heightinmeter ** 2)

    if BMIindex < 18.5:
        print("You are Underweight")

    elif (BMIindex >= 18.5) and (BMIindex < 25.0):
        print("You are Normal")

    elif (BMIindex >= 25.0) and (BMIindex < 30.0):
        print("You are Overweight")

    else:
        print("You are Obese")

else:
    print("Please input number")