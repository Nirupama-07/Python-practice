text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

# Convert both strings to lowercase
text1 = text1.lower()
text2 = text2.lower()

# Check if lengths are equal
if len(text1) != len(text2):
    print("Not an Anagram")
else:
    # Sort both strings
    if sorted(text1) == sorted(text2):
        print("Anagram")
    else:
        print("Not an Anagram")