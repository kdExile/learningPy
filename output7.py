


def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c==2

def main():
    l=[1,2,3,4,5,6,7,8,9]
    l1=[]
    for i in range(len(l)):
        l1.append(l[i]**2)
    print(l1)#[1,4,9,...,81]

    
    l2=[l[i]**2 for i in range(len(l))] 
    print(l2)

    
    l3=[l[i]**3 for i in range(len(l)) if i%2==0]
    print(l3)

    
    n=int(input('enter range'))
    l4=[i for i in range(1,n+1)]
    print(l4)
    l5=[i for i in l4 if prime(i)]
    print(l5)

    #l=[ list_element(with operations, if any) for i in l {if any conditions}]
    #above is known as LIST COMPREHENSION


main()


