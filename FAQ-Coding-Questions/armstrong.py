num=int(input("Enter a number:"))

temp=num
total=0

while num>0:
    digit=num%10
    total+=digit**3
    num//=10

if total==temp:
    print("Armstrong")
else:
    print("Not armstrong")

#armstrong: 153=1^3 + 5^3 + 3^3=153