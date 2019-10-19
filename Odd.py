#odd numbers between a range
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
for i in range(start,end+1):
   if i%2!=0:
      print(i)
print("Successfully Printed all odd number between range")
