def Piglatin():
    word=input("enter a word ")
    word=word.lower()
    for i in range(len(word)):
        if word[i] in "aeiou":
             word=word[i:]+word[:i]
             break
    word=word+"ay"
    print("piglatin form:",word)
Piglatin()
            
            
