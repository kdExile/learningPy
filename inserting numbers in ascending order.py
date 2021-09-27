#no duplicates, no sort()
def main():
    n=int(input("enter number of elements"))
    l=[]
    l.append(int(input("enter a number")))
    i=0
    while i<(n-1):
        x=int(input("enter a number"))
        j=0
        if x not in l:
            i+=1
            while j < len(l):
                if x<l[j]:
                    l.insert(j,x)
                    break
                j+=1
            else:
                l.append(x)
        
    print(l)
    
main()    
            
            
        
