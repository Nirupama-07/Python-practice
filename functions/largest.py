num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

def largest(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

print("Largest number is:",largest(num1,num2))