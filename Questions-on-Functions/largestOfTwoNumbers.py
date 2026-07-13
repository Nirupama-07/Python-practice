num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

'''def largest(num1,num2):
    if num1>=num2:
        print(num1,"is largest")
    else:
        print(num2,"is largest")

largest(num1,num2)'''

#by using Lambda function

largest = lambda num1, num2: num1 if num1 >= num2 else num2
print(largest(num1, num2))