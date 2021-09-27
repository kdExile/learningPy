def show():
    n=int(input("enter number of rows"))
    m=int(input("enter number of columns"))
    l2=[]
    for i in range(n):
        l=[]
        for j in range(m):
           l.append(int(input("enter number")))
        l2.append(l)
    return l2,n,m

def display(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j],' ',end='')
        print()
        
def calculate():
    l,r,c=show()
    a,p,q=show()
    print("first matrix:")
    display(l)
    print("second matrix:")
    display(a)
    if c!=p:
        return False
    x=[]
    for i in range(r):
        v=[]
        for j in range(q):
            b=0
            for k in range(c):#p can also be used instead of c since both are equal
                b+=l[i][k]*a[k][j]
            v.append(b)
        x.append(v)
    print("matrix obtained after multiplication:")        
    return x
    
def main():
    x=calculate()
    if x==False:
        print("Matrix Multiplication is not possible")
    else:
        display(x)
main()    
    
        
        
            
            
        

