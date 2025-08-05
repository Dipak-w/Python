import math

# Input coefficients
a = float(input("Enter coefficient a (a ≠ 0): "))
while a == 0:
    print("Coefficient 'a' cannot be zero.")
    a = float(input("Enter coefficient a (a ≠ 0): "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate discriminant
discriminant = b**2 - 4*a*c

# Find two solutions
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"The equation has two real solutions: {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"The equation has one real solution: {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print(f"The equation has two complex solutions: {real_part}+{imaginary_part}j and {real_part}-{imaginary_part}j")



# Write a Python program to swap two variables without temp variable

a = 5
b = 10
# swapping without a temporary variable
a, b = b, a

print("after swapping: a =", a, ", b =", b)


#Write a Python Program to Check if a Number is Positive, Negative or Zero

number = float(input("Enter a number:"))
if number > 0:
    print("The number is positive,")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


import pyjokes
joke = pyjokes.get_joke()
print("Here's a joke for you:", joke)  



