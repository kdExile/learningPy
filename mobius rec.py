def mobius(n,i,c):
    if n==1:
        return (-1)**c
    elif n%i==0 and n//i%i==0:
        return 0
    else:
        if n%i==0:
            n,c=n//i,c+1
        return mobius(n,i+1,c)
    
def mobius1(n,i):
    if n==1:
        return 1
    elif n%i==0 and n//i%i==0:
        return 0
    else:
        x=1
        if n%i==0:
            n,x=n//i,-1
        
        return x*mobius1(n,i+1)
    
def main():
    l=[6,12,30,210,75]
    for i in l:
        print(mobius1(i,2))
        print(mobius(i,2,0))
main()
    
