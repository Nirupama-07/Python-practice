# Python-practice
Python coding problems and solutions for interview preparation, covering fundamentals, OOP, file handling, functions, and more.

## Topics

- Conditional Statements
- Loops
- Functions
- Exception Handling
- File Handling
- OOPS-Basics(Classes,Objects,Constructors)
- OOPS-Advanced(Encapsulation,Abstraction)
- Django (company_site)
-- Install Django, Tailwind, setup the django and done django fundamentals along with MVT
-- Done Templates and static files
-- Completed models and all ORM
-- Completed forms.Form and forms.ModelForm


## Tricks to remember logics
# Python Logic Cheatsheet

## 🔹 Extract the Last Digit

* Use `% 10`
* Example:

  * `1234 % 10 = 4`

**Used in:**

* Count Digits
* Sum of Digits
* Reverse Number
* Palindrome Number
* Armstrong Number

---

## 🔹 Remove the Last Digit

* Use `// 10`
* Example:

  * `1234 // 10 = 123`

**Used in:**

* Count Digits
* Sum of Digits
* Reverse Number
* Palindrome Number
* Armstrong Number

---

## 🔹 Count Digits

* Initialize `count = 0`
* Remove one digit at a time.
* Increase `count` after each removal.
* Stop when the number becomes `0`.

---

## 🔹 Sum of Digits

* Initialize `sum = 0`
* Extract the last digit.
* Add it to `sum`.
* Remove the last digit.
* Repeat until the number becomes `0`.

---

## 🔹 Reverse Number

* Initialize `reverse = 0`
* Extract the last digit.
* Append it to `reverse` using:

  * `reverse = reverse * 10 + digit`
* Remove the last digit.
* Repeat until the number becomes `0`.

---

## 🔹 Palindrome Number

* Store the original number.
* Reverse the number.
* Compare:

  * `original == reverse` → Palindrome
  * Otherwise → Not Palindrome

---

## 🔹 Armstrong Number

* Store the original number.
* Count the total number of digits (`n`).
* Extract each digit.
* Raise it to the power `n`.
* Add all the powered digits.
* Compare the sum with the original number.

---

## 🔹 Fibonacci Series

* Start with `0` and `1`.
* Next number = Previous number + Current number.
* Move the values forward and repeat.

---

## 🔹 Factorial

* Start with `factorial = 1`.
* Multiply by every number from `1` to `n`.

---

## 🔹 Prime Number

* Check if the number is divisible by any number from `2` to `√n`.
* If divisible → Not Prime.
* Otherwise → Prime.

---

## ⭐ Common Pattern for Digit-Based Problems

```
Extract Last Digit  →  % 10
        ↓
Perform Required Operation
        ↓
Remove Last Digit  →  // 10
        ↓
Repeat until Number becomes 0
```


## Purpose

- Improve Python programming skills
- Prepare for technical interviews
- Practice problem solving
