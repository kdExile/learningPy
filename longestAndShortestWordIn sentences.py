def longestAndShortestWordInASentence(s):
    l=s.split()
    mx=l[0]
    mn=l[0]
    m=len(mx)
    n=len(mn)
    for i in l[1:]:
        if len(i)>=m:
            if len(i)==m:
                mx=mx+' '+i
            else:
                mx=i
                m=len(mx)
            
        if len(i)<=n:
            if len(i)==n:
                mn=mn+' '+i
            else:
                mn=i
                n=len(mn)
    
    return {'longest':mx,'shortest':mn}
def main():
    n=int(input('enter number of sentences'))
    l=[]
    for i in range(n):
        l.append(longestAndShortestWordInASentence(input('enter a sentence')))
    print(l)
main()
    
