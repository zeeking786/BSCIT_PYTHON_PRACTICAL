"""
Implement the concept of inheritance using python
"""

#Single Level Inheritance 

class Parent():
	def fun1(self):
		print("This is Parent class")

class Child(Parent):
	def fun2(self):
		print("This is Child Class")

ob = Child()
ob.fun1()
ob.fun2()
