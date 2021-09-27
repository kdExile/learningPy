def boundaryElementsSum(l):
    s=0
    for i in range(len(l)):
        for j in range(len(l[i])):
            if i==0 or i==len(l)-1 or j==0 or j==len(l[i])-1:
                s+=l[i][j]
        
    return s
def sortedArray(l):
    a=[]
    for i in range(len(l)):
        for j in range(len(l[i])):
            a.append(l[i][j])
    bdsum1=boundaryElementsSum(l)
    
    a=sorted(a)
    v=0
    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i][j]=a[v]
            v+=1
    
    bdsum2=boundaryElementsSum(l)
    return bdsum1,bdsum2
def display(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j],' ',end='')
        print()
def main():
    n=int(input("enter number of rows"))
    m=int(input("enter number of columns"))
    l2=[]
    for i in range(n):
        l=[]
        for j in range(m):
           l.append(int(input("enter number")))
        l2.append(l)
    display(l2)
    print()
    bdsum1,bdsum2=sortedArray(l2)

    print("sum before sort:",bdsum1)
    print("sorted array:")
    display(l2)
    print()
    print("sum after sort:",bdsum2)

main()

















            
