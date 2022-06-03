# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code heres
    lower_word=word.lower()
    lower_anagram=anagram.lower()
    word_list=list(lower_word)
    anagram_list=list(lower_anagram)
    checklist=[]
    for i in anagram_list:
        if i in word_list:
            word_list.remove(i)
            checklist.append(i)
    result=len(checklist)==len(anagram_list)
    if result is True:
        return True
    else:
        return False

print(find_anagram('table','belta'))
