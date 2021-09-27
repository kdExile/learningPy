def main():
    n=int(input("enter a number"))
    copy=n
    l=[]
    while n>0:
        l.append(n%10)
        n//=10
    l=l[::-1]
    s=sum(l)
    #print(l)
    while s<copy:
        i=1
        while i<len(l):
            l[i-1]=l[i]
            i+=1
        l[-1]=s
        print(l)
        s=sum(l)
    print(l)   
    if s==copy:
        print("Keith Number")
    else:
        print("not a Keith number")
main()
