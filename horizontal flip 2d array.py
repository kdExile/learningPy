#horizontal flip
def main():
    m=int(input("enter number of rows"))
    n=int(input("enter number of columns"))
    r=[]
    for i in range(m):
        c=[]
        for j in range(n):
            c.append(int(input("enter a number")))
        r.append(c)
    print (r)
    lr=[]
    for i in range(m):
        l=[]
        for j in range(n):
            l.append(r[i][n-1-j])
        lr.append(l)
    print(lr)
main()
    
