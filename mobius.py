def mobius(n):
    a=2
    s=0
    c=0
    while n>1:
        if n%a==0:
               #s=s+1
               c=c+1
               if (n//a)%a ==0:
                   return 0
               
               n=n//a
              # if s>1 :
                   #return 0
        else:
                a=a+1
                #s=0
        
           
               
                
            
            
    return (-1)**c
def main():
    #n=int(input("enter a number"))
    l=[24,35,30,5,90,70]
    for i in l:
        print(i,":",mobius(i))
main()
        
