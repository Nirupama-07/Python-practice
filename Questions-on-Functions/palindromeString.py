text=input("Enter a text:")

def checkPalindrome(text):
    temp=text
    rev=""
    for i in text:
        rev=i+rev
    
    if rev==temp:
        print("Palindrome")
    else:
        print("Not a palindrome")

checkPalindrome(text)