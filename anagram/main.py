def print_anagram(word, anagram):
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
            print('this is an anagram')
            return True
    else:
        print('this is not an anagram')
        return False

print(print_anagram('table','belta'))