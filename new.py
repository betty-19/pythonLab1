# def num():
#     num1 = int(input("Enter the Number: "))
#     if num1 % 2==0:
#      print(str(num1) + " is even")
#     else:
#      print(str(num1) + " is odd")
# num()

# n = int(input("Enter The Number "))
# if n % 3 ==0:
#     print("Hello")
# elif int (n) % 5==0:
#         print ("World")
# elif int (n) % 3==0 and int (n) % 5==0:
#     print ("Hello World")
# elif int (n) % 3 != 0 and int (n) % 5!=0:
#     print ("The Number is Not Divisible By Either 3 or 5")

d = input("Enter the number")
match int(d):
    case 2:
        print ("No")
    case 4:
        print("Yes")
    case _:
        print ("Invalid Input")    