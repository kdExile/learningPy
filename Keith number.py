def main():
    n=int(input("enter a number"))
    l=[n//100,n//10%10,n%10]
    s=sum(l)
    #print(l)
    while s<n:
        l[0],l[1],l[2]=l[1],l[2],s
        #print(l)
        s=sum(l)
    if s==n:
        print("Keith Number")
    else:
        print("not a Keith number")
main()
