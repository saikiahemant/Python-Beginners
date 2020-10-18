# Function to compute GCD of two numbers using recursion
def gcd(a,b):
    if(b==0): # Base case
        return a
    else:
        return gcd(b, a%b) # Recursive call

# Function to find LCM
def LCM(a,b):
    return int((a * b) /gcd(a, b)) # lcm * hcf = a*b
# Tester code
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
LCM = LCM(a,b)
print("L.C.M is: ")
print(LCM)