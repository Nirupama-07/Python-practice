'''def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

terms = int(input("Enter number of terms: "))

for i in range(terms):
    print(fibonacci(i), end=" ")'''

def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

terms = int(input("Enter number of terms: "))
fibonacci(terms)