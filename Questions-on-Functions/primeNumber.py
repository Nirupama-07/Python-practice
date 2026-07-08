'''num=int(input("Enter a number:"))

def prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        print("Prime")
    else:
        print("Not a prime number")

prime(num)'''

def prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False

    return True


num = int(input("Enter a number: "))

if prime(num):
    print("Prime")
else:
    print("Not a Prime")