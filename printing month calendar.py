def accept():
    m=int(input("enter month"))
    y=input("enter year")
    return m,y
def valid(d):
    dmy=d.replace('/',"")
    return len(d)==10 and d[2]=='/' and d[5]=='/' and dmy.isdigit()
def leap(y):
    return y%400==0 or y%4==0 and y%100!=0
def dayFind(m,y):
    m=str(m)+'/'
    y=str(y)
    date='01/'+m+y
    
    
    d=date.split('/')
    d1=int(d[0])
    d2=int(d[1])
    d3=int(d[2])
    l=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if leap(d3):
        l[2]=29

    
    
    
        
    day=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    d=0
        
    for i in range(1,d3):
        if leap(i):
            d+=366
        else:
            d+=365
        
    for i in range(1,d2):
        d+=l[i]
    d+=d1
    return(day[d%7])
        
    
        
def main():
    m,y=accept()
    s=dayFind(m,y)
    p=[]
    l=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    a=0
    if leap(int(y)):
        l[2]=29
    day=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    for i in range(7):
        if s==day[i]:
            a=i
            
            
    for i in range(5):
        q=[]
        for j in range(7):
            q.append('  ')
        p.append(q)
        
    b=1
    
    m=int(m)
    for i in range(5):
        for j in range(7):
            x=' 'if b//10==0 else ''
            
            if i==0 and j>=a:
                
                p[i][j]=x+str(b)
            else:
                if i>0:
                   p[i][j]=x+str(b)
                else:
                    b-=1
            
            b+=1
            if b>l[m]:
                break
    
    if b<=l[m]:
        for i in range(1):
            for j in range(7):
                p[i][j]= x+str(b)
                b+=1
                if b>l[m]:
                    break
            
                
        
    for i in range(5):
        for j in range(7):

    
            print(p[i][j],' ',end='')
        print()
main()
    
