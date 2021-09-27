def main():
    name=input("enter a name")
    s=''
    name1=''.join(name)
    
#method 1    
    while True:
        x=name.find(' ')
        if x==-1:
            s=name+' '+s
            break
        else:
            s+=name[0]+' '
            name=name[x+1:]
    print(s)

#method 2    
    s=''
    c=0    
    while True:
        x=name1.find(' ',c)
        if x==-1:
            s=name1[c:]+' '+s
            break
        else:
            s+=name1[c]+' '
            c=x+1        
    print(s)


#using rfind()
    c=-1
    while True:
        x=name1.rfind(' ')
        if x==-1:
            print (name1)
            break
        else:
            print(name1[x+1:])
            name1=name1[:x]
       
main()
            
            
            
