def prime(n):
    c=0
    for i in range(1,n//2+1):
        if n%i==0:
            c=c+1
    return c==1
def reverse(n):
    r=0
    while n>0:
        r=r*10+n%10
        n//=10
    return r
def main():
    l=int(input('enter lower range '))
    u=int(input('enter upper range '))
    for i in range(l,u+1):
        r=reverse(i)
        if prime(i) and prime(r) and r!=i:
            print(i,'is an emirp number ')
    #prime fibonacci terms
    n=int(input('enter  range '))
    a=0
    b=1
    i=1
    while i<=n:
        if prime(a):
            print(a)
            i=i+1
        c=a+b
        a=b
        b=c
    #s=2+3+5+7+11+13+.........n terms
    n=int(input('enter  range '))
    a=0
    b=1
    i=1
    while i<=n:
        if prime(b):
            print(b)
            i=i+1
            a=a+b
        b=b+1
    print(a)

        
        
            
main()

#dd/mm/yyyy
# y%400==0 or y%4==0 and y%100!=0






