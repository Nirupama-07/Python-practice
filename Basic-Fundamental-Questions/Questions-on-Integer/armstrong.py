num=int(input("Enter a number:"))

temp=num
total=0

while num>0:
    digit=num%10
    total+=digit**3
    num=num//10

if temp==total:
    print("Armstrong")
else:
    print("Not a armstrong number")