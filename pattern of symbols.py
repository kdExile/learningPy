def main():
    n=int(input('enter order of square matrix'))
    symbol1=input('enter first symbol (which will form the diagonal)')
    symbol2=input('enter second symbol(which will form the upper and lower triangles)')
    symbol3=input('enter third symbol(which will form the right and left triangles)')
    l=[]
    for i in range(n):
        a=[]
        for j in range(n):
            k=n-i-1
            if j==i or j==(k):
                a.append(symbol1)
            elif j>i and j<k or j<i and j>k :
                a.append(symbol2)
            else:
                a.append(symbol3)
        l.append(a)
    for i in range(n):
        for j in range(n):
            print(l[i][j],end='')
        print()
main()    
