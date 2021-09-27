def valid(dt):
    dmy=dt.replace('/',"")
    if len(dt)==10 and dt[2]=='/' and dt[5]=='/' and dmy.isdigit():
        d=int(dt[:2])
        m=int(dt[3:5])
        y=int(dt[6:])
        if y>0 and m>0 and m<13 and d>0 and d<=countDay(m,y):
            return True
    return False
            
def countDay(m,y):
    d=0
    if m==4 or m==6 or m==9 or m==11:
        d=30
    elif m==2:
        d=29 if y%400==0 or y%100!=0 and y%4==0 else 28
    else:
        d=31
    return d
def change(s):
    return s[6:]+s[3:5]+s[:2]
def main():
    
    n=int(input('enter number of persons'))
    l=[]
    i=0
    while i<n:
        
        name=input('enter name')
        dmy=input("enter date in dd/mm/yyyy format")
        if valid(dmy):
            r=[name,dmy]
            l.append(r)
            i+=1

    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if change(l[j][1]) > change(l[j+1][1]):
                l[j],l[j+1]=l[j+1],l[j]

    f=open('person.txt','w')
    for i in l:
        f.write(str(i)+'\n')
        
    f.close()
    f=open('person.txt')
    for i in f:
        print(i,end='')
    f.close()
main()        
        


    












    
    


    
