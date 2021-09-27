def commonWordsAndFrequency(s1,s2):
    l1=s1.split()
    l2=s2.split()
    l=[]
    c=[]
    for word in l1:
        for w in l2:
            if word==w and word not in l:
                l.append(word)
                c.append(l1.count(word)+l2.count(word))
    return l,c
def main():
    s1=input("enter a sentence")
    s2=input("enter a sentence")
    l,c=commonWordsAndFrequency(s1,s2)
    if len(l)==0:
        print("no common words")
    else:
        print("common words and their frequency:")
        for i in range(len(l)):
            
            print(l[i],c[i])

main()
        
    
    
