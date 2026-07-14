text=input("Enter a text:")

upperCount=0
lowerCount=0

for i in text:
    if i.isupper():
        upperCount+=1
    elif i.islower():
        lowerCount+=1
print(upperCount,lowerCount)