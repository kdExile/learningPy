def check(n):
    for i in range(n):
        if i+(i+1)==n:
            return True,i,i+1
    return False,0,0
def main():
    n=int(input('enter number of elements'))
    l=[]
    for i in range(n):
        l.append(int(input('enter a number')))
    print(l)
    for i in range(n):
        x,y,z=check(l[i])
        if x:
            print(l[i],'=',y,'+',z)
         
main()
        
                 

                 
                 

                
