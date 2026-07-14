text=input("Enter a text:")

vowel=['a','e','i','o','u']
count=0

for i in text:
    if i in vowel:
        count+=1
    
print(count)