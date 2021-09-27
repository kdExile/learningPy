
def main():
    n=input('enter expression')
    l=[]
    flag=True
    for i in range(len(n)):
        if n[i]=='(':
            l.append(n[i])
        if n[i]==')':
            if len(l)==0:
                flag=False
            else:
                l.pop()
            
  
    if len(l)!=0 or not flag:
        print('brackets not properly matched')
    else:
        print('brackets properly matched')
main()
        
    
