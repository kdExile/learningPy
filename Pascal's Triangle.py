def factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
def nCr(n,r):
    return factorial(n)//(factorial(r)*factorial(n-r))
def Pascal(n):

    for i in range(1,n+1):
        sp=n-i
        print(' '*sp,end='')
        for j in range(i+1):
            if i==1 and j==0:
                print(' ',end='')
                continue
            else:
                print(nCr(i,j),'',end='')    
        sp-=1
        print()
def main():
    n=int(input("enter number of lines"))
    Pascal(n)
main()
