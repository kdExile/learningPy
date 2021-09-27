def main():
    r=int(input('enter number of rows'))#3
    c=int(input('enter number of columns'))#4
    l=[]
    for i in range(r):
        a=[]
        for j in range(c):
            a.append(int(input('enter a number')))
        l.append(a)
    print(l)
    m=r*c #12
    for i in range(m-1):
        for j in range(m-1-i):
            if l[j//c][j%c] > l[(j+1)//c][(j+1)%c]:
                l[j//c][j%c],l[(j+1)//c][(j+1)%c]=l[(j+1)//c][(j+1)%c],l[j//c][j%c]
    print(l)
   
main()
