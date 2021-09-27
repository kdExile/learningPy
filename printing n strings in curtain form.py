
def main():
    n=int(input("enter number of strings"))
    l=[]
    m=[]
    for i in range(n):
        s=(input("enter string"))
        l.append(s)
        m.append(len(s))
    p=max(m)
    for i in range(n):
        l[i]+=' '*(p-len(l[i]))
    print(l)
    for i in range(p):
        for j in range(n):
            print(l[j][i],'    ',end='')
        print()
    

main()
        
        















                
