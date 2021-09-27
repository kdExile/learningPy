import pickle
def main():
    #d={'John':'2002-09-15','Jodie':'2001/10/05','Jack':'2001-10-20','Jennifer':'2002/08/15'}
    '''n=int(input('enter number of persons'))
    d={}
    for i in range(n):
        name=input("enter name")
        date=input("enter date of birth in yyyy/mm/dd")
        d[name]=date
    f=open('friends.dat','wb')
    pickle.dump(d,f)
    f.close()'''
    f=open('friends.dat','rb')
    d={}
    d=pickle.load(f)
    print(d)
    f.close()
    l=list(d.values())
    print(l)
    for i in range(len(l)):
        l[i]=l[i].replace('/','-')
    print(l)
        
    k=list(d.keys())
    '''for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                k[j],k[j+1]=k[j+1],k[j]'''
    m=sorted([l[i]+'-'+k[i] for i in range(len(l))])
    #print(m)
    p={}
    for i in range(len(l)):
        #p[k[i]]=l[i]
        p[m[i][11:]]=m[i][:10]
    
    print(p)
    
       

main()














#method chaining-involves class methods called using dot operator.It is evaluated left to right.
#s='  good morning   '
#l=s.strip().upper().split()
#function chaining-involves built-in methods and is evaluated right to left.
#n=int(input('enter number of persons'))
