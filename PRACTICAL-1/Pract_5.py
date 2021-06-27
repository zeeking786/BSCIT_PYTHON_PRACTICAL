"""
Write a function to check the input value is Armstrong
and also write the function for Palindrome.
"""

def Armstrong(n):
  temp=n
  result=0
  while(temp!=0):
    remainder=temp%10
    result=remainder**3+result
    temp=temp//10

  if(result==n):
    print(n," is armstrong number ")
  else:
    print(n, "not an armstrong number ")

def Palindrome(n):
  temp=n
  reverse=0
  while(temp!=0):
    remainder=temp%10
    reverse=reverse*10+remainder
    temp=temp//10

  if(n==reverse):
    print(n," is Palindrome")
  else:
    print(n," is not Palindrome")

n=int(input("Enter a number :- "))
Armstrong(n)
Palindrome(n)
