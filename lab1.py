
from unittest import result


def sum():
    print("Hello world")
    
    x = float(input("Enter first number"))
    y = float(input("Enter second number"))
    
    result = x+y
    
    print(result)
   
    
    name = "Haileab"
    age = 22
    
    print("My name is {:s} and I am {:d}".format(name,age))
    
    x,y,z = "Orange","Banana","Apple"
    
    print(x,y,z)
    
    a = 2
    b = 2.5
    
    print(type(b))
    
    x = "Haileab"
    print(len(x))
    
sum()

