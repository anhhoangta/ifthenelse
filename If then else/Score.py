__author__ = 'anhhoangta'


while True:
    inputscore = input("Enter Your Score: ")

    if inputscore.isnumeric() and int(inputscore) <= 100 and int(inputscore) >=0:
        score = int(inputscore)

        if score >= 90:
            print("grade is A")

        elif score >= 80:
            print("grade is B")

        elif score >= 70:
            print("grade is C")

        elif score >= 60:
            print("grade is D")

        else:
            print("grade is F")

    else:
        print("Not a number. Input again")