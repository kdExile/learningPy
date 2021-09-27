def main():
    #n=int(input("enter number of books"))
    '''f=open('bookstore.txt','a')
    for i in range(n):
        t=input("enter name of book")
        a=input("enter name of author")
        g=input("enter genre")
        p=float(input("enter price"))
        q=int(input("enter quantity"))
        f.write(t+', '+a+', '+g+', '+str(p)+', '+str(q)+'\n')
    f.close()'''
    f=open('bookstore.txt')
    '''for d in f:
        print(d)'''
    print(type(f.read()))
    f.close()
    

    
    
main()
