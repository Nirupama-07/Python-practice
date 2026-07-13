num=int(input("Enter a number:"))

rev=0
temp=num

while num>0:
    digit=num%10
    rev=rev*10+digit
    num//=10

if rev==temp:
    print("Palindrome Number")
else:
    print("Not a palindrome")