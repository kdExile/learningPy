def valid(d):
    dmy=d.replace('/',"")
    return len(d)==10 and d[2]=='/' and d[5]=='/' and dmy.isdigit()
def countDay(m,y):
    d=0
    if m==4 or m==6 or m==9 or m==11:
        d=30
    elif m==2:
        d=29 if y%400==0 or y%100!=0 and y%4==0 else 28
    else:
        d=31
    return d
def main():
    dmy=input("enter date in dd/mm/yyyy format")
    f=False
    if valid(dmy):
        d=int(dmy[:2])
        m=int(dmy[3:5])
        y=int(dmy[6:])
        if y>0 and m>0 and m<13 and d>0 and d<=countDay(m,y):
            f=True
    if f:
        print(dmy,"is a valid date")
    else:
        print(dmy,"is not a valid date")
main()
