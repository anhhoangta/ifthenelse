__author__ = 'anhhoangta'

inputscore = input("Enter Your Score: ")
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