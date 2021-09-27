def listRearrangement(l,a):
    x=list(l)
    for i in range(a):
        k=l[0]
        for j in range(1,len(l)):
            l[j-1]=l[j]
        l[-1]=k
    return l
            
        
def main():
    n=int(input("enter number of elements"))
    l=[]
    for i in range(n):
        l.append(int(input("enter a number")))
    print(l)
    a=int(input("enter number of places you want to shift"))
    print(listRearrangement(l,a))
    #l[a:]+l[:a]
main()
    
        
    
