def typeOfVowels():
    s=input("enter  a sentence")
    s=s.lower()
    c=0
    t=['a','e','i','o','u']
    u=[0,0,0,0,0]
    for ch in s:
        if ch in t:
            u[t.index(ch)]+=1
    for i in range(len(u)):
        if u[i]==0:
            c+=1
    print("type of vowel:",5-c)
typeOfVowels()
            
        
