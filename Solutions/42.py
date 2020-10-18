"""
42. program to Reverse a Sentence Using Recursion
"""

def power(base, pow):
    if pow == 0:
        return 1
    if pow == 1:
        return base
    result = power(base, pow-1) * base
    return result

base =int(input("Enter your base: "))
pow = int(input("Enter the power: "))

print("{} raised to the power {} is {} ".format(base, pow, power(base,pow)))