"""
Implement the concept of inheritance using python
"""

#Multilevel Inheritance

class Parent():
	def fun1(self):
		print("This is Parent class")

class Child1(Parent):
	def fun2(self):
		print("This is Child1 class")
class Child2(Child1):
	def fun3(self):
		print("This is Child2 class")

ob = Child2()
ob.fun1()
ob.fun2()
ob.fun3()
