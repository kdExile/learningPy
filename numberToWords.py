def main():
    n=int(input("enter a number"))
    t1=("",'one','two','three','four','five','six','seven','eight','nine')
    t2=('ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen')
    t3=('','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety')
    if n==0:
        wd="zero"
        
        return
    
    wd=''
    if n<0:
        wd='minus'+" "
         
    n=abs(n)
    if n//100>0:
        wd+=t1[n//100]+" hundred "
    n=n%100
    f=n//10
    l=n%10
    
    if f==1:
        wd+=t2[l]
    else:
        wd+=t3[f]+" "+t1[l]
    
   
    print(wd)
    

             
main()                   
         
        
         
         
        
            
            
                 
             
            
 

