"""
Write a Python program to read last n lines of a file.
"""

def read_lastnlines(fname,n):
	with open('file.txt') as f:
		for line in (f.readlines() [-n:]):
			print(line)

read_lastnlines('file.txt',2)
