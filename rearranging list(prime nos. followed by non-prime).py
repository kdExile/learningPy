#rearranging list such that prime numbers are in the beginning followed by the non prime numbers
def prime(n):
    ct=0
    for i in range(1,n+1):
        if n%i==0:
            ct+=1
    return ct==2
def main():
    n=int(input("enter range"))
    l=[]
    l_new=[]
    
    for i in range(n):
        l.append(int(input("enter number")))
        
    for element in l:
        if prime(element):
            l_new.append(element)
            
    for element in l:
        if element not in l_new:
            l_new.append(element)
                 
    print(l_new)
main()
            
            
        
        
