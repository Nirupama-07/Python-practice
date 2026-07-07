digit=int(input("Enter a number:"))

sum=0

while digit>0:
    sum=sum+(digit%10)
    digit//=10
print(sum)