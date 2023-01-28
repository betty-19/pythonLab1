# #def sum():
#     #print("Hello World")

# #sum()

# x,y,z = "Orange","Banana","Apple"

# print(x,y,z)

# a = 2
# b = 2.1
# print(type(b))
# print(type(a))

# name="kaleab"
# height=1.7

# print("my name is {:s} and i am {:f} meters tall".format(name,height))
import re

def remove_punctuation(s):
    return re.sub(r'[^\w\s]', '', s)

# Example usage
text = "Hello, World! This:: {} is a test."
print(remove_punctuation(text)) # Output: "Hello World This is a test"