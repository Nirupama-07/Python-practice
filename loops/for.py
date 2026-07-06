#Write a program to print numbers from 1 to 10 using for
'''for i in range(1,11):
    print(i)'''

#Write a program to print each character of a string.
'''char=input("Enter a string: ")

for ch in char:
    print(ch)'''

#Write a program to find the sum of numbers in a list.
'''lst=[10,20,30]
sum=0
for item in lst:
    sum=sum+item
print(sum)'''

#Write a program to count vowels in a string.
text=input("Enter a text: ")
count=0
vowel=['a','e','i','o','u']
for ch in text:
    if(ch in vowel):
        count+=1
print(count)