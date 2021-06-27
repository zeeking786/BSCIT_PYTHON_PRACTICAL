"""
Write a Python program to print a specified list after
removing the 0th, 2nd, 4th and 5th elements.
"""

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']  
color = [x for (i,x) in enumerate(color) if i not in (0,2,4,5)]  
print(color)
