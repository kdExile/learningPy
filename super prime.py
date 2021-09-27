'''2,3,5,7,11,13,17,19,23,29,31
1,2,3,4,5,6,7,8,9,10,11
3-2,5-3,11-5,17-7,31-11'''
import math
def prime(a):
    c=2
    while c<=int(math.sqrt(a)) and a%c!=0:
        c+=1
    return a>1 and c>int(math.sqrt(a))

def main():
    n=int(input('enter number of terms'))             
    l=[]
    a=2
    c=0
    i=1
    while i<=n:
        if prime(a):
            c+=1
            if prime(c):
                print(a,c)
                l.append(a)
                i+=1
        a+=1
    print(l)
        
    
main()
        
    
