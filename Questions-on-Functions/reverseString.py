#Method 1
'''def reverse(text):
    rev=""

    for i in text:
        rev=i+rev
    return rev

text=input("Enter a text:")
print(reverse(text))'''

#Method 2
text=input("Enter a text")
def reverse(text):
    return text[::-1]

print(reverse(text))