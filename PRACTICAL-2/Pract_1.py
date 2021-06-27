"""
Write a function that takes a character (i.e. a string of length 1)
and returns True if it is a vowel, False otherwise.
"""

print ("Function to check whether a char is vowel or not")
 
def vowelChecker (inputChar):
    if (inputChar == "a" or inputChar == "A" or
        inputChar == "e" or inputChar == "E" or
        inputChar == "i" or inputChar == "I" or
        inputChar == "o" or inputChar == "O" or
        inputChar == "u" or inputChar == "U" or
        inputChar =="aeiou" or inputChar =="AEIOU"):
        return True
    else:
        return False
 
print ("Enter the string to check")
inputChar = input()
 
if vowelChecker(inputChar) == True:
    print("The enterted character is Vowel")
else:
    print("The enterted character is not Vowel")
