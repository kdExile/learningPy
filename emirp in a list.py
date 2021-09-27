def prime(n):
    c=0
    for i in range(1,n//2+1):
        if n%i==0:
            c=c+1
    return c==1
def reverse(n):
    r=0
    while n>0:
        r=r*10+n%10
        n//=10
    return r

def check(l):
    x=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if prime(l[i]) and prime(reverse(l[i])) and l[i]==reverse(l[j]) and x.count(l[i])==0 and x.count(l[j])==0:
                x.append(l[i])
                x.append(l[j])

    return x
def main():
    n=int(input("enter number of elements"))
    a=[]
    for i in range(n):
        a.append(int(input("enter a number")))
    x=check(a)
    if len(x)==0:
        print("no emirp number")
    else:
        for i in range(0,len(x),2):
            print('(',x[i],',',x[i+1],')')
    
main()
        
            
            
                
    
    
    
