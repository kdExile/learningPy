#lucky number
def main():
    n=int(input("enter range"))
    l=[]
    for i in range(1,n+1):
        l.append(i)
    print (l)
    c=2
    while c<=len(l):
        j=0
        m=[]
        while j<len(l):
            if (j+1)%c!=0:
                m.append(l[j])
            j+=1
        l=m.copy()
        c+=1
    print("lucky number(s):",l)
    print()
    lucky(n)

def lucky(n):
    l=[]
    for i in range(1,n+1):
        l.append(i)
    print (l)
    c=2
    while c<=len(l):
        j=c-1
        while j<len(l):
            l.remove(l[j])
            j+=c-1
        c+=1
        print(l)
    print ("lucky number(s):",l)
    
    
main()
