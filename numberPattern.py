def main():
    n=int(input('enter number of lines'))
    m=n*(n+1)//2-1
    i=0
    j=0
    
    for i in range(1,n+1):
        print(" "*(n-i),sep="",end="")
        for j in range(1,i+1):
            if m>9:
                print(m," ",end="")
            else:
                print(m,"  ",end="")
            m=m-1
        print()
main()
    
