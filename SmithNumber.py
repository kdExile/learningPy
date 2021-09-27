def digitsum(n):
    s=0
    while n>0:
        s=s+n%10
        n=n//10
    return s
def Smith(n):
    a=2
    s=0
    copy=n
    while n>1:
        if n%a==0:
            n=n//a
            s=s+digitsum(a)
        else:
            a=a+1
    
    if s==digitsum(copy):
        print(copy,"is a Smith number")
    else:
        print(copy,"is not a Smith number")
def main():
    n=int(input("enter a number "))
    Smith(n)
main()
