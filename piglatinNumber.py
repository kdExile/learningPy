import math
def sumOfDigits(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s
def prime(num):
    f=0
    flag=False
    for i in range(num):
        if (num%(i+1))==0:
            f=f+1
    if f==2:
        flag=True
    return flag
def Piglatin(n):
    new=0
    d=int(math.log(n,10))+1
    dsum=sumOfDigits(n)
    ct_dsum=int(math.log(dsum,10))+1
    
    flag=False
  
    num=n
    for i in range(1,d+1):
        dig=num//(10**(d-i))
        x=i-1
        
        if prime(dig):
            flag=True
            new=n%(10**(d-x))
            
            new=new*(10**x)
            
            new=new+(n//(10**(d-x)))
           
            new=new*(10**(ct_dsum))+dsum
            
            return new
        num=num%(10**(d-i))
    if flag==False:
        new=dsum*(10**d)+n
        return new
    
def main():
    n=int(input("enter number"))
    print("piglatin form:",Piglatin(n))
main()
    
