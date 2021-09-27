def insertingNumbersInAscendingOrder():
    n=int(input("enter number of elements"))
    l=[]
    l.append(int(input("enter a number")))
    i=0
    while i<(n-1):
        x=int(input("enter a number"))
        j=0
        while j < len(l):
            if x<l[j]:
                    l.insert(j,x)
                    break
            j+=1
        else:
            l.append(x)
        i+=1
    return l,n

def intersection(p,q):
    x=[]
    for i in p:
        if i in q and i not in x:
            x.append(i)
            
    return x
    
def union(p,q):
    p.extend(q)
    v=[]
    for i in p:
        if i not in v:
            v.append(i)
    for j in q:
        if j not in v:
            v.append(j)
    return v
    

            
    
def main():
    p,m=insertingNumbersInAscendingOrder()
    q,n=insertingNumbersInAscendingOrder()
       
    #print(p)
    #print(q)
    
    print("Intersection:",intersection(p,q))
    print("Union:",union(p,q))
main()
    
    
