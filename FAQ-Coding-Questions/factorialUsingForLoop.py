num=int(input("Enter the number of which you want the factorial:"))

fact=1

for i in range(0,num+1):
    if i==0:
        fact=1
    else:
        fact=fact*i
print(fact)