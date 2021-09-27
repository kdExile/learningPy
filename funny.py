def funny(n):
    m=n*2-1
    c=-1
    for i in range(1,m+1):
        print("*",end="")
        if i<=m//2+1:
            c=c+1
        else:
            c=c-1
            
        for j in range(c):
            print("  ",end="")
        if i>1 and i<m:
            print("*")
        else:
            print()
def main():
    n=int (input("Enter number of lines"))
    funny(n)
main()
