def valid(d):
    dmy=d.replace('/',"")
    return len(d)==10 and d[2]=='/' and d[5]=='/' and dmy.isdigit()
def leap(y):
    return y%400==0 or y%4==0 and y%100!=0
def main():
    date=input("enter date in dd/mm/yyyy format")
    f=True
    if not valid(date):
        f=False
    else:
        
        d=date.split('/')
        d1=int(d[0])
        d2=int(d[1])
        d3=int(d[2])
        l=[0,31,28,31,30,31,30,31,31,30,31,30,31]
        if leap(d3):
            l[2]=29
        if not (d3>0 and d2>0 and d2<13 and d1>0 and d1<=l[d2]):
            f=False
    
    
    
        if f:
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
            print(day[d%7])
        
    if not f:
        print("ask someone to gift you a calendar on new year!")
        
        
        
    
main()
    
