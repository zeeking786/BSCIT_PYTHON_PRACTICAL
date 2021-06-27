"""
Create a class called Numbers, which has a single class attribute called MULTIPLIER,
and a constructor which takes the parameters x and y (these should all be numbers).
i. Write a method called add which returns the sum of the attributes x and y.
ii. Write a class method called multiply, which takes a single number parameter a
and returns the product of a and MULTIPLIER.
iii. Write a static method called subtract, which takes two number parameters, b
and c, and returns b - c.
iv. Write a method called value which returns a tuple containing the values of x
and y. Make this method into a property, and write a setter and a deleter for
manipulating the values of x and y.
"""


class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
    
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
obj=cal(a,b)
choice=1

while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",obj.add())
    elif choice==2:
        print("Result: ",obj.sub())
    elif choice==3:
        print("Result: ",obj.mul())
    elif choice==4:
        print("Result: ",round(obj.div(),2))
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
 
print()
