import string

def remove_punctuation(s):
    # create a translator object to remove punctuation
    translator = str.maketrans('', '', string.punctuation)

    # use the translator
    return s.translate(translator)

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
