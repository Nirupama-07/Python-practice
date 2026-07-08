text=input("Enter a text")
def count_vowels(text):
    count=0
    vowels=('a','e','i','o','u')
    
    for i in text:
        if i in vowels:
            count+=1
    return count
    
    if count>0:
        print(count)
    else:
        print("There is no vowels")
print(count_vowels(text))