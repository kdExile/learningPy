def prime(num):
    f=0
    flag=False
    for i in range(num):
        if (num%(i+1))==0:
            f=f+1
    if f==2:
        flag=True
    return flag
def series():
    n=(int)(input("Enter number of terms"))
    x=(int)(input("Enter value of x"))
    a=0
    b=1
    c=0
    s=0
    pn=2
    i=1
    add=0
    while i<=n:
        if prime(pn):
            p=x**pn
            print("power",pn)
            c=a+b
            s=s+b
            print("denominator",s)
            a=b
            b=c
            add=add+(p/s)
            i=i+1
        pn=pn+1
    print ("sum=",add)
series()


        
    
    
            
            
        
                
            
                
                
            
            
            
        
