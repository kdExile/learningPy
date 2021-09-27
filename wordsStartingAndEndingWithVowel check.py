#words starting and ending with vowel-->bring vowels first then consonant;other words-->arrange them
def vowel(l):
    return "aeiouAEIOU".find(l)!=-1
def main():
    word=input("enter word")
    x=sorted(word,key=vowel,reverse=True)
    print(''.join(x))

main()

def myMethod():
    s=input("enter a sentence")
    l=[]
    s=s+' '
    c=0
    i=0
    while i<len(s):
        i=s.find(' ',i)
        word=s[c:i]
        l.append(word)
        i+=1
        c=i
    sent=""
    wd=''
    vowel='aeiouAEIOU'
    for word in l:
        if word[0] in vowel and word[-1] in vowel:
            for letter in word:
                if letter in vowel:
                    wd=wd+letter
                    word=word.replace(letter,'')
            wd+=word
        else:
            wd=''.join(sorted(list(word),reverse=True))
        sent=sent+wd+" "
        wd=''
    print ("new sentence is:",sent)

