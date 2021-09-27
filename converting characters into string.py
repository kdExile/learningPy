def main():
    n=int(input("enter number of characters"))
    l=[]
    i=1
    while i<=n:
        x=input("enter a character")
        if len(x)==1:
            l.append(x)
            i+=1
    print(l)
    t=''
    for ch in l:
        t+=ch
    print(t)
main()
