#sieve of Eratosthenes
import math
def main():
    n=int(input("enter range"))
    l=[]
    for i in range(2,n+1):
        l.append(i)
    print (l)
    sqrt=(int)(math.sqrt(n))
    for i in range(sqrt):
        j=i+1
        while j<len(l):
            if l[j]%l[i]==0:
                l.remove(l[j])
            j+=1
        
    print("prime numbers:",l)
main()
        
        
    
    
