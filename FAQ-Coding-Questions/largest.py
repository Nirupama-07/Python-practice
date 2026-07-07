#WAP to calculate the largest of two numbers
'''num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

if num1>num2:
    print(num1,"is greatest")
else:
    print(num2,"is greatest")'''

#WAP to calculate the greatest of three numbers

'''num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

if (num1>=num2 and num1>=num3):
    print(num1,"is greatest")
elif(num2>=num1 and num2>=num3):
    print(num2,"is greatest")
elif(num3>=num1 and num3>=num2):
    print(num3,"is greatest")
else:
    print("Invalid data")'''

#WAP to Find Greatest Using Nested If
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))

if num1>num2:
    if num1>num3:
        print(num1,"is greatest")
    else:
        print(num3,"is greatest")
else:
    if num2>num3:
        print(num2,"is greatest")
    else:
        (num3,"is greatest")