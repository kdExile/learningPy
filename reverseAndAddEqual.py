def reverse(n):
    rev=0
    while n>0:
        rev=rev*10+(n%10)
        n//=10
    return rev

    
def main():
    n=int(input("Enter a number"))
    ct=1
    flag=False
    while ct<=10:
        print(reverse(n),n)
        if reverse(n)==n:
            flag=True
            break
        else:
            n=n+reverse(n)
        ct=ct+1
    if flag==True:
        print("good number")
    else:
        print("bad number")
    n=5
    for i in range (1,n+1):
        print(" "*(n-i),"*"*i,sep="")
    print(2**4**2)
    print(id(n))
main()

            
    
    
    
    
    
