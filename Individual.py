string = input("Enter a string: ")

# Initialize an empty dictionary
char_frequency = {}

# Iterate through each character in the string
for char in string:
    # If the character is already in the dictionary, increment its count
    if char in char_frequency:
        char_frequency[char] += 1
    # If the character is not in the dictionary, add it with a count of 1
    else:
        char_frequency[char] = 1

# Print the character frequency count
print(char_frequency)