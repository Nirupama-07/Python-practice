num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))

def largest(num1,num2,num3):
    if num1>num2:
        if num1>num3:
            print(num1,"is largest")
        else:
            print(num3,"is largest")
    else:
        if num2>num3:
            print(num2,"is largest")
        else:
            print(num3,"is largest")

largest(num1,num2,num3)