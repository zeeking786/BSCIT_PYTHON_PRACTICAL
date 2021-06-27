"""
Write a Python program to clone or copy a list
"""

orgList = [22, 33, 44, 55, 66, 77, 88, 99]
print("Original List Items = ", orgList)

newList = []
newList.extend(orgList)
print("New List Items      = ", newList)
