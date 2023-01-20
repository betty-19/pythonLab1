from collections import Counter

string = input("Please enter a string: ")

char_freq = Counter(string)


print("Character frequency count:")
for char, count in char_freq.items():
    if char == ' ':
        print('spaces: ', count)
    else:
        print(char, ":", count)