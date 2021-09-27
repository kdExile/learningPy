def main():
    n=int(input("enter number of lines"))
    a=[]
    a.append([1,1])
    k=1
    for i in range(1,n):
        l=[]
        j=1
        b=1
        while j<=i+1:
            l.append(b)
            b=a[i-1][j-1]
            if j<=i:
                b+=a[i-1][j]
            j+=1
        l.append(1)
        a.append(l)

        
    for i in range(n):
        sp=n-i
        print(' '*sp,end='')
        for j in range(i+2):
            if i==0 and j==0:
                print(' ',end='')
                continue
            else:
                print(a[i][j],end=' ')
        sp-=1
        print()
            
    
main()



'''1
121
1331
14641
151051 '''
