#Write a program using nested if to check login username and password.
'''username = "Rakesh"
password = 1234
login = True

name = input("Enter username: ")
passw = int(input("Enter password: "))

if name == username:
    if passw == password:
        if login:
            print("Login successful")
        else:
            print("Account disabled")
    else:
        print("Invalid password")
else:
    print("Invalid username")'''

#Write a program using nested if to check whether a number is positive and even.
number=int(input("Enter a number: "))

if number>0:
    if number%2==0:
        print(number,"is positive and even")
    else:
        print(number,"is odd")
else:
    print(number,"is negative")
