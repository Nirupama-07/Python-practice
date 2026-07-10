#Write a program to handle division by zero.
'''try:
    num=10/0
    print(num)
except ZeroDivisionError:
    print("Cannot be divide by zero")'''

#Write a program to handle invalid integer input.
'''try:
    num=int(input("Enter a number:"))
    print(num)
except ValueError:
    print("Enter integer value")'''

#Write a program to handle list index out of range.
'''try:
    lst=["Apple","Banana",7,25.5]
    print(lst[7])
except IndexError:
    print("Index out of range")'''

#Write a program to handle missing dictionary key.
'''try:
    dictionary={
        "name":"Nirupama",
        "roll":22
    }
    print(dictionary['age'])
except KeyError:
    print("Key not available")'''

#Write a program using try, except, and finally
'''try:
    name=input("Enter username:")
    password=int(input("Enter password:"))
    
    if (name=="admin" and password==1234):
        print("Login successfully")
    else:
        print("Invalid user")
    

except ValueError:
    print("Enter valid details")

finally:
    print("You are always welcome")'''

#Write a program using try, except, else, and finally
'''try:
    grade=int(input("Enter your marks:"))

    if grade>90:
        print("A+")
    elif grade>80:
        print("B")
    elif grade>70:
        print("C")
    else:
        print("Fail")
except ValueError:
    print("Enter marks of your subject")
else:
    print("Try best")
finally:
    print("Thankyou for visiting")'''

#Write a program to raise an exception if age is less than 18.
age = int(input("Enter your age: "))

if age < 18:
    raise Exception("Age must be 18 or above.")
else:
    print("You are eligible.")

    