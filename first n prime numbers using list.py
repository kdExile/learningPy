def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    return False

def main():
    n=int(input("enter range"))
    l=[]
    c=0
    i=1
    while c<n:
        if prime(i):
            l.append(i)
            c+=1
        i+=1
    print(l)
main()
        
