def vowelByNextVowel():
    w=input("enter a word")
    w=w.upper()
    d='AEIOUA'
    s=''
    for ch in w:
        i=d.find(ch)
        if i!=-1:
            s+=d[i+1]
        else:
            s+=ch
    print(s)
vowelByNextVowel()
        
