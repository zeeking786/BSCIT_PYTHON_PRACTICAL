"""
Implement the concept of inheritance using python
"""

#Multiple Inheritance

class Parent1():
	def fun1(self):
		print("This is Parent1 class")
class Parent2():
	def fun2(self):
		print("This is Parent2 class")

class Child(Parent1, Parent2):
	def fun3(self):
		print("This is Child class")

ob = Child()
ob.fun1()
ob.fun2()
ob.fun3()
