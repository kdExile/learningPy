def main():
    f=open('MOV Act4 Sc1.txt',encoding='utf8')
    n=input('enter name of character')
    a=[]
    n=n.upper()
    v=''
    
    for line in f:
        l=line.split()
        if len(l)==1:
            v=l[0]
        if v==n:
            a.append(line)

    for i in range(len(a)):
        print(a[i],end='')
        
    f.close()
main()
                    
                    
            
      
        
            
                
