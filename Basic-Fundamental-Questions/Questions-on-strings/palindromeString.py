text=input("Enter a string to check palindrome:").lower()
rev=""

for i in text:
    rev=i+rev
if rev==text:
    print("Palindrome")
else:
    print("Not a palindrome")