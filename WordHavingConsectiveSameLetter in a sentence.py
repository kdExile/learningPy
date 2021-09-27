#printing words with consecutive letters in a sentence
def isWordHavingConsecutiveSameLetter(word):
    for i in range(0,len(word)-1):
        if word[i]==word[i+1]:
            return True
    return False
def main():
    sentence=input("enter a sentence")
    word=''
    sentence=sentence+" "
    for ch in sentence:
        if ch!=' ':
            word=word+ch
        else:
            if isWordHavingConsecutiveSameLetter(word):
                print (word)
            word=""
main()
    
