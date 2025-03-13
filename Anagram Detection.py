word = input("Type a word : ")
word2 = input("Type a word again : ")
def Anagram_Detection(word, word2):
    word = word.upper().replace(" ","")
    word2 = word2.upper().replace(" ", "")
    return sorted(word) == sorted(word2)
print(Anagram_Detection(word, word2))