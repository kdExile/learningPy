def main():
    n=input('enter name')
    s=''
    l=n.title().split()
    c=l[0]+' '
    for i in l[1:-1]:
        c+=i[0]+'.'
    c+=' '+l[-1]
    print(c)
    for i in range(len(l)):
        if i==0 or i==len(l)-1:
            s+=l[i]+' '
        else:
            s+=l[i][0]+'.'
    print(s)
main()
    
