#transpose of a matrix
def main():
    m=int(input("enter number of rows"))
    n=int(input("enter number of columns"))
    r=[]
    for i in range(m):
        c=[]
        for j in range(n):
            c.append(int(input("enter a number")))
        r.append(c)
    for i in range(m):        
        print (r[i])
    lr=[]
    for i in range(n):
        l=[]
        for j in range(m):
            l.append(r[j][i])
        lr.append(l)
    for i in range(n):        
        print (lr[i])
main()
