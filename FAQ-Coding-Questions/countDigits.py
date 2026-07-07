#if the input is a string
'''digit=input("Enter any number:")

print(len(digit))'''

#if the input is a integer
digit=int(input("Enter a digit:"))

count=0

while digit>0:
    count+=1
    digit//=10
print(count)
