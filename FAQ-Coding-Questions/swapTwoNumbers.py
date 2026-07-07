#WAP to swap two numbers by using a third variable
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

'''temp=num1
num1=num2
num2=temp

print(num1,num2)'''

#without using third variable
num1,num2=num2,num1

print(num1,num2)