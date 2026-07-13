num=int(input("Enter a number:"))

temp=num
sum=0

while num>0:
    digit=num%10
    sum=sum+(digit**3)
    num//=10

if temp==sum:
    print("Armstrong")
else:
    print("Not an armstrong")