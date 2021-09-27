def anagramCheck(w1,w2):
    
    if len(w1)!= len(w2):
        return False
    
    for ch in w1:
        if w1.count(ch)!=w2.count(ch):
            return False
        
    return True

'''def listWithoutRepetitionOfWords(l1):
    
    l=[]
    for word in l1:
         if  word not in l:
            l.append(word)
    
    return l'''

def check(l):
    
    #l= listWithoutRepetitionOfWords(l)
    #print(l)
    x=''
    c=len(x)
    
    for i in range(len(l)-1):
        
        
        for j in range(i+1,len(l)):
            if anagramCheck(l[i],l[j])  :
                if x.find(l[i])==-1 :
                    x+=l[i]+' '+l[j]+' '
                elif x.find(l[j])==-1:
                    x+=l[j]+' '
                
                
                
        if len(x)!=c:
                x+='\n'
                c=len(x)
                 
                
    return x


def main():
    
    #n=int(input("enter number of words"))
    words=['read','dear','read','deer','dare','lived','good','devil','lived','dare']
    v=False
    
    '''for i in range(n):
        words.append(input("enter word"))'''
        
    #l=check(words).split('#')
    
    
    '''for i in range(len(l)):
        if l[i]!=' ' and l[i]!='':
            print(l[i],'is a group of anagrams')
            v=True'''
    
    x=check(words)
    if len(x)==0:
        print("no anagrams in given list")
    else:
        print(x)
        
main()
    
