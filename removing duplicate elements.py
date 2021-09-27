def main():
    n=int(input("enter number of elements"))
    l=[]
    i=0
    for i in range(n):
        x=(input("enter any value"))
        if x.isdigit():
            x=int(x)
        elif not x.isalpha():
            x=float(x)
            
        l.append(x)
    print (l)
    i=0
    while i<len(l)-1:
        j=i+1
        while j<len(l):
            if l[i]==l[j]:
                l.remove(l[j])
            j+=1
        i+=1
        
    print(l)
main()
