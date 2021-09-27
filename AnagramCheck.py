
def anagramCheck(w1,w2):
    if len(w1)!= len(w2):
        return False
    for ch in w1:
        print(ch,w1.count(ch))
        print(ch,w2.count(ch))
        if w1.count(ch)!=w2.count(ch):
            return False
    return True
def main():
    word1=input("enter word")
    word2=input("enter word")
    word1=word1.lower()
    word2=word2.lower()
    if(anagramCheck(word1,word2)):
        print("anagram")
    else:
        print("not anagram")
   
main()
