text = input("Enter a string: ")

lst = text.split()

longestLength = 0
longestWord = ""

for word in lst:
    length = len(word)

    if length > longestLength:
        longestLength = length
        longestWord = word

print("Longest word:", longestWord)
print("Length:", longestLength)