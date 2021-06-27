"""
Write a Python program to append text to a file and display the text.
"""

testfile =  open("file.txt", "a")
testfile.write("Hope you all are fine...\n")
testfile.close()

appended_file = open("file.txt", "r")
print(appended_file.read())
