string = input("Please enter a string: ")
count = {} 
  
for i in string: 
    if i in count: 
        count[i] += 1
    else: 
        count[i] = 1
  
print ("Character Frequency Count is :\n " +  str(count))