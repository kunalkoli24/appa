# Write a program non-recursive and recursive program to calculate Fibonacci numbers and 
# analyze their time and space complexity.

# Non-Recursive (Iterative) Fibonacci Program

""" 
#Take input from the user
nterms = int(input("How many terms: "))

# First two terms
n1, n2 = 0, 1
count = 0

# Check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence up to", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1, end=" ")  # Print the current term
        nth = n1 + n2       # Update for the next term
        # Update n1 and n2
        n1 = n2
        n2 = nth
        count += 1
"""


# Recursive Fibonacci Program
"""
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Take input from the user
nterms = int(input("How many terms: "))

# Check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(fibonacci_recursive(i), end=" ")
"""
