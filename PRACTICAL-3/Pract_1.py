"""
A pangram is a sentence that contains all the letters of the English alphabet at least once,
for example: The quick brown fox jumps over the lazy dog. Your task here is to write a
function to check a sentence to see if it is a pangram or not.
"""

def ispangram(str):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for char in alphabet:
		if char not in str.lower():
			return False

	return True
	
# Driver code
string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True):
	print("Yes")
else:
	print("No")
