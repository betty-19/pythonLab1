num = input("Enter a number ")
for x in range(1 ,int(num) + 1):
    if int(x) % 3== 0 and int(x)% 5 != 0:
        print("Hello " + str(x))
    elif int(x)%5 == 0 and int(x)% 3 != 0:
        print("world " + str(x))
    elif int(x) %3 ==0 and int(x) % 5== 0:
        print("Hello World "+ str(x))
n= input("Enter a number to make square ")
for x in range(int(n)):
    for y in range(int(n)):
        print("* ", end="")
    print()
L =input("Enter length ")
w =input("Enter width ")
for x in range(int(L)):
    for y in range(int(w)):
        print("* ", end="")
    print()