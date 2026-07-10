#Write a program to count the frequency of each character in a string.

text=input("Enter a text")

frequency={}


for i in text:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
for key,value in frequency.items():
    print(key,":",value)