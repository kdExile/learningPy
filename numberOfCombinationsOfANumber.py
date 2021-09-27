def numberOfDigits(n):
    if n==0:
        return 1
    c=0
    while n>0:
        c+=1
        n=n//10
    return c
def frequency():
    n=int(input("enter number "))
    c=n
    
    comb=fac(numberOfDigits(c))
    f=0
    
    for i in range(0,10):
        
        f=0
        n=c
        while n>0:
            d=n%10
            if d==i:
                f+=1
            
             
            n=n//10
        
        if f>1:
            comb=comb//fac(f)
    print("number of combination(s):",comb)
def fac(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

            
frequency()
    

    
    
