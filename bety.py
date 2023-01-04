#first program
def sum():
    print("Hello")
print("Hello world")
sum()
x,y,z="yabu","kaleab","Haileab"
print(x)
k=w=s=7
print(z)
a=3
b=3.5
print(type(b))
print(len(y))
name=input("Enter your name ")
num1=input("Enter the first number ")
num2=input("Enter the second number ")
sum = int(num1) + int(num2)
print("the sum of two number is " + str(sum))
name = "betelhem"
print(name)
age = 8
cgpa = 6.77896785
print("my name is {:s} and i am {:d} years old. my cgpa is {:f}".format(name,age,cgpa) )
#new
name3 = "Abebe"
array="hello, world"
print(array.split(','))
print(name3[-3:-1])
print(name3[::-1])
print(bin(60))
print(str(bin(name3)))
#age=input("")
num = input("Enter a number to check if it is even or odd")
if int(num) % 2 == 0:
    print("It is even")
else:
    print("It is odd")
#new
if int(num) % 3== 0 and int(num)% 5 != 0:
    print("Hello")
elif int(num)%5 == 0 and int(num)% 3 != 0:
    print("world")
elif int(num) %3 ==0 and int(num) % 5== 0:
    print("Hello World")
#new
num = input("Enter a number to check if it is even or odd ")
match int(num):
    case 1:
        print("It is one")
    case 2:
        print("It is two")
    case 3:
        print("It is three")
    case _:
        print("invalid input")