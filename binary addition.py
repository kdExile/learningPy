def  binToDec(n):
    n=int(n)
    s=0
    i=0
    while n>0:
        s+=(n%10)*(2**i)
        i+=1
        n//=10
    return s
def decToBin(n):
    r=0
    f=1
    while n>0:
        r=r+f*(n%2)
        f*=10
        n//=2
    return r

def main():
    n=int(input("enter a number"))
    m=int(input("enter another number"))
    
    p=str(decToBin(n))
    q=str(decToBin(m))
    print(binToDec(p))
    a=len(p)
    b=len(q)
    p='0'*(max(a,b)-a)+p
    q='0'*(max(a,b)-b)+q
    
    l=[]
    for i in range(len(p)+1):
        l.append(0)

    p=list(p)
    q=list(q)
    r=''
    i=-1
    while i>=-(len(p)):
        p[i]=int(p[i])
        q[i]=int(q[i])
        if p[i]+q[i]+l[i]==2:
            l[i]=0
            l[i-1]=1
            
        elif p[i]+q[i]+l[i]==3:
            l[i]=1
            l[i-1]=1
            
        else:
            l[i]=p[i]+q[i]+l[i]

        r=str(l[i])+r
        i-=1
    r=str(l[0])+r
    print(p)
    print(q)
    print(l)
    print(r)

    print(binToDec(r))
    
    
main()
