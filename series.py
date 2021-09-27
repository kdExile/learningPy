def reverse(n):
    rev=0
    while n>0:
        rev=rev*10+(n%10)
        n//=10
    return rev
def series_1():
    n=int(input("enter number of terms"))
    s=0
    t=0
    for i in range(1,n+1):
        t=t*10+i
        if i%2==0:
            s=s+reverse(t)
            print (reverse(t)," ",end="")
        else:
            s=s+t
            print (t," ",end="")
    print("Sum:",s)
series_1()
def series_2():
    n=int(input("enter number of terms"))
    s=0
    t=0
    for i in range(1,n+1):
        t=t*10+i
        if i%2!=0:
            s=s+reverse(t)
            print (reverse(t)," ",end="")
        else:
            s=s+t
            print (t," ",end="")
    print("Sum:",s)
series_2()
          
