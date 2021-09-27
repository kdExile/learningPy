def recdet(l):
    if len(l)==2 and len(l[0])==2:
        return l[0][0]*l[1][1]-l[0][1]*l[1][0]
    else:  
     c=0
     s=0
    for i in range(len(l)):
        s+=(-1)**c*l[0][i]*recdet(finddet(l,i))
        c+=1
    return s
       

'''Algorithm
1   method that accepts a 2Dlist returns a 2D list which is the determinant'''
def finddet(l,n):
    l1=[]
    for i in range(1,len(l)):
        l2=[]
        for j in range(len(l)):
            if j !=n:
                l2.append(l[i][j])
        l1.append(l2)
    return l1
def main():
    n=int(input("enter number of rows"))
    l2=[]
    for i in range(n):
        l=[]
        for j in range(n):
           l.append(int(input("enter number")))
        l2.append(l)
    print(recdet(l2))
main()
    

        
