"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that
tells them the year that they will turn 100 years old.
"""

name = input('Enter your name: ')
age = input('Enter your age: ')
year = 2018 - int(age) + 100
message = name + ' will be 100 years old in ' + str(year) + '\n'
print(message)

