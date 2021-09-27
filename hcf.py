def hcf(a,b):
    n=a
    m=b
    while b>0:
        r=a%b
        a=b
        b=r
    print("hcf:",a)
    
    while m>0:
        n,m=m,n%m
    print("hcf",n)
    
hcf(12,8)
