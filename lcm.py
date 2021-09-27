def lcm(a,b):
    x=a
    while x%b!=0:
        x=x+a
    return x
def hcf(a,b):
    while b>0:
        a,b=b,a%b
    return a
    
def main():
    a=int(input("enter first number"))
    b=int(input("enter second number"))
    print("HCF is",hcf(a,b))
    print("LCM is",lcm(a,b))
    n=int(input("enter number of terms"))
    h=int(input("enter a number"))
    l=h
    p=h
    for i in range(1,n):
        n=int(input("enter a number"))
        h=hcf(h,n)
        l=lcm(l,n)
        p=p*n
    print("hcf is",h)
    print("lcm is",l,"?",p//h)
        
    
main()
