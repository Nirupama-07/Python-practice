'''num=int(input("Enter a number:"))

def square(num):
    return num*num
print("Square of",num,"is:",square(num))'''

#by the use of lambda function
x=int(input("Enter a number"))
square=lambda x: x*x

print(square(x))
