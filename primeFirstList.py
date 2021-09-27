def prime(n):
    ct=0
    for i in range(1,n+1):
        if n%i==0:
            ct+=1
    return ct==2
def main():
    n=int(input("enter range"))
    l=[]
    for i in range(n):
        l.append(int(input("enter number")))
    c=0
    for i in range(0,n):
        if prime(l[i]):
            t=l[i]
            for j in range(i,c,-1):
                l[j]=l[j-1]
            l[c]=t
            c+=1
    print(l)
main()
