import os
def main():
    f=open('bookstore.txt')
    f1=open('temp.txt','w')
    n=input('enter name of author')
    a=[]
    b=False
    for line in f:
        if n in line:
            l=line.split(',')
            a.append(l)
            print('book:',l[0],',price:',l[3])
            b=True
    if not b:
        print("sorry no books available!")
    else:
        s=input('enter name of the book')
    for i in range(len(a)):
        if s==a[i][0]:
            if int(a[i][4])>0:
                print("Yes you can go ahead and buy!")
                v=input('enter Y if you agree')
                
                if v.upper()=='Y':
                    k=i
                    p=int(a[i][4])-1
                    a[i][4]=str(p)
                    
                    
                    
            else:
                print("currently unavailable!")
    f.seek(0)
    for line in f:
        l=line.split(',')
        if l[0]==a[k][0]:
            f1.write(','.join(a[k])+'\n')
        else:
            f1.write(line)
    print("book details:")
    
    print(','.join(a[k][:-1]))
    
    


    f1.close()
    f.close()
    os.remove('bookstore.txt')
    os.rename('temp.txt','bookstore.txt')
    
   
main()
