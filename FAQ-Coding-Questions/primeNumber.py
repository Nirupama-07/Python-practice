# is a number is a prime number or not
'''num=int(input("Enter a number:"))

count=0

for i in range(1,num+1):
    if num%i==0:
        count+=1

if count==2:
    print("Prime number")
else:
    print("Not a prime number")'''

#print all the prime numbers between 1 and 100

for num in range(2,101):
    count=0 

    for i in range(1,num+1):
        if num%i==0:
            count+=1
    
    if count==2:
        print(num)