num=int(input("Enter a number:"))


rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print(rev)

# % is used to extract the last digit while // is used to extract the digits other than the last