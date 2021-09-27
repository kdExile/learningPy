def main():
    n=int(input("enter number of books"))
    f=open('my favourite books.txt','a')
    for i in range(n):
        t=input("enter name of book")
        a=input("enter name of author")
        g=input("enter genre")
        p=float(input("enter price"))
        f.write(t+', '+a+', '+g+', '+str(p)+'\n')
    f.close()
    f=open('my favourite books.txt')
    for d in f:
        print(d)
    f.close()
    
main()
