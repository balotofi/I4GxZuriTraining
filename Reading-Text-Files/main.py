# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(f"{filename}.txt") as file_text:
        contents = file_text.read()
        return contents


def count_words():
    text = read_file_content("story")
    # [assignment] Add your code here
    word_bank = dict()
    for line in text:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        for word in words:
            if word in word_bank:
                word_bank[word] = word_bank[word] + 1
            else:
                word_bank[word] = 1
    for key in list(word_bank.keys()):
        print(key, ":", word_bank[key])


count_words()