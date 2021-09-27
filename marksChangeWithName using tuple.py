def main():
    t1=('Anwesha','Asmita','Preeti','Koushiki','Annewsa','Divyasree','Ranjabati')
    t2=(70,80,90,95,85,75,77)
    print(t1)
    print(t2)
    for i in t1:
        print(i,"is your marks correct?")
        a=int(input("enter 0 for no and 1 for yes"))
        if a==0:
            b=int(input("enter new marks"))
            j=t1.index(i)
            l1=list(t2)
            l1[j]=b
            t2=tuple(l1)
    print (t1)
    print(t2)
main()
