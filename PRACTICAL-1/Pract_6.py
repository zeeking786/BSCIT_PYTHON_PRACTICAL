"""
Write a recursive function to print the factorial for a given number.
"""

def factorial(n):
    if (n==1 or n==0):
        return 1
	
    else:
        return (n * factorial(n - 1))

num = int(input("Enter the number :"))
print("number : ",num)
print("Factorial : ",factorial(num))
