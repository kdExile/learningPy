def longestConsonantSubstring():
    word=input("enter a word ")
    l=[]
    ln=[]
    s=""
    
    for ch in word:
        if ch not in "aeiouAEIOU":
            s=s+ch
        if ch in "aeiouAEIOU":
            l.append(s)
            ln.append(len(s))
            #print(s)
            s=""
    n=len(ln)
    ln.sort()
    for i in range(0,n):
        if len(l[i])==ln[n-1] and ln[n-1]!=0:
            print ("longest consonant substring",l[i])
    if len(l)==0:
        print("longest consonant substring",word)
    
        
           
longestConsonantSubstring()     
            
            
        

        
        
        
