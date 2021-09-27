import csv
def main():
    n=int(input('enter number of students'))
    f=open('student.csv','w',newline='')
    w=csv.writer(f)
    h=['Name','English','Maths','Physics','Chemistry','Computer Science']
    l=[]
    l.append(h)
    for i in range(n):
        name=input('enter name')
        a=float(input('enter marks(E)'))
        b=float(input('enter marks'))
        c=float(input('enter marks'))
        d=float(input('enter marks'))
        e=float(input('enter marks'))
        r=[name,a,b,c,d,e]
        l.append(r)
    w.writerows(l)
    f.close()

    f=open('student.csv','r')
    g=csv.reader(f)
    m=[]
    for i in g:
        print(i)
        m.append(i)
    f.close()

    f1=open('result.csv','w',newline='')
    p=csv.writer(f1)
    v=[]
    for i in m[1:]:
        x=sorted(i[2:])
        i=i[:2]+x[1:]
        v.append(i)
    p.writerows(v)
    f1.close()

    f1=open('result.csv')
    q=csv.reader(f1)
    for i in q:
        print(i)
    f1.close()
    
main()
        
        
















    
    
    
