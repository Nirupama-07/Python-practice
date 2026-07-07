#Build a Calculator Using if-elif

num1=int(input("Enter a number"))
num2=int(input("Enter second number"))

operation=input("Enter the operation")

if operation=='+':
    print(num1+num2)
elif operation=="-":
    if num1>num2:
        print(num1-num2)
    else:
        print(num2-num1)
elif operation=="*":
    print(num1*num2)
elif operation =="/":
    print(num1/num2)
else:
    print("Give a valid number")