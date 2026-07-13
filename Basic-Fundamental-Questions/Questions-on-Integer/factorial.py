#WAP to find the factorial of a number

num=int(input("Enter a number:"))

def factorial(num):
    if(num==1):
        return 1
    else:
        return num * factorial(num-1)
print(factorial(num))