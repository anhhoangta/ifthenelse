__author__ = 'anhhoangta'

#print the title of program
print("\r")
print("Mutiplication Table".center(38))

#print the first two lines
print("{:4}".format(""),end="")
for num in range(1,10):
    print("{:2d}" .format(num), end="\t")   #the first line
print()
print("-"*38)       #the 2nd line

<<<<<<< HEAD
#print remanning lines use nested for loop2396
=======
#print remanning lines use nested for loop
>>>>>>> origin/master
for i in range(1,10):
    print("{:d}|".format(i),end="\t")   #print the first column
    for j in range(1, 10):
        print("{:2d}" .format(i*j),end="\t")    #print ixj with margin-right
    print()
<<<<<<< HEAD
print()
=======
print()
>>>>>>> origin/master
