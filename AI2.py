import string

def remove_punctuation(s):
    # create a translator object to remove punctuation
    translator = str.maketrans('', '', string.punctuation)

    # use the translator
    return s.translate(translator)
def compute_char_frequency(text):
    # create a dictionary to store the character frequencies
    char_freq = {}

    # count the frequency of each character
    for char in text:
        char = char.lower()
        if char in char_freq:
            char_freq[char] += 1
        else:
            if char == " ":
                continue
            else:
                char_freq[char] = 1
    # sort the characters by frequency in decreasing order
    sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

    # print the first five most frequently occurring characters
    for char, freq in sorted_chars[:5]:
        print(f'{char}: {freq}')
def compute_word_frequency(text):
    # split the text into words
    words = text.split()

    # create a dictionary to store the word frequencies
    word_freq = {}

    # count the frequency of each word
    for word in words:
        word = word.lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # sort the words by frequency in decreasing order
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    # print the word frequencies
    count =0
    for word, freq in sorted_words:
        print(f'{word}=> {freq}, ' ,end=" ")
        count = count + 1
        if count == 5:
            print()
            count=0
    print()

def main():
    # open the text file for reading
    with open('Assignment.txt', 'r', encoding="utf-8") as f:
        # read the text
        text = f.read()

        # remove punctuation from the text
        text = remove_punctuation(text)

        # compute and print the word frequency
        print("****Enter your choice****")
        print("1.To know word frequency")
        print("2.To know the character frequency")
        print("3.To know the Total line")
        print("4.To know the Total words")
        print("5.To know the Total  number of character")
        print("6.Exit")
    while(True):
           user_input = input("Enter you choice: ")
           match int(user_input):
               case 1:
                  compute_word_frequency(text)
               case 2:
                   compute_char_frequency(text)
               case 3:
                   num_lines = text.count('\n') + 1
                   print(f'\nTotal lines: {num_lines}')
               case 4:
                   num_words = len(text.split())
                   print(f'Total words: {num_words}')
               case 5:
                   num_chars = len(text)
                   print(f'Total characters: {num_chars}')
               case 6:
                    break

if __name__ == '__main__':
    main()
