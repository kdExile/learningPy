def recprime(n,i=2):
    if n>1 and i*i>n:
        return True
    elif n<2 or n%i==0:
        return False
    else:
        return recprime(n,i+1)


def twinprime(n):
    l=[]
    if recprime(n):
        if recprime(n-2):
            l.append(n-2)
        if recprime(n+2):
            l.append(n+2)
    if len(l)>0:
        if l[0]<n:
            l.insert(1,n)
        else:
            l.insert(0,n)
    if len(l)>0:
        print(l[0],l[1])
        if len(l)==3:
            print(l[1],l[2])
    return l
    
    
def main():
    n=int(input('enter a number'))
    a,b=n,n
    c=0
    if len(twinprime(n))>0:
        return
    while True:
        a+=1
        b-=1
        if len(twinprime(b))>0:
            c+=1
        if len(twinprime(a))>0:
            c+=1
        if c>0:
            break
main()
            
        

        

            

        




    
