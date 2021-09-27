def badAnagram():
    word1=input("enter a word")
    word2=input("enter a word")
    word1=word1.lower()
    word2=word2.lower()
    d=0
    if len(word1)==len(word2):
        for ch in word1:
            if word1.count(ch)!=word2.count(ch) :
                print("not anagram")
                d=1
                break
        
    else:
        print("not anagram")
       
    if d==0:
        print("anagram")
badAnagram()
