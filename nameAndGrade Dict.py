def initials():
    n=input("enter name")
    a=''
    l=n.split()
    i=0
    
    for w in l:
        i+=1
        if i == 1:
            a+=w+' '
        elif i==len(l):
            a=w+','+a
        else:
            a+=w[0]+'.'
    print(a)
    return a

def calcGrade(m):
    if m>=90:
        g='A'
    elif m>=70:
        g='B'
    elif m>=50:
        g='C'
    elif m>=35:
        g='D'
    else:
        g='E'
    return g

def main():
    n=initials()
    marks=float(input("enter average marks"))
    grade=calcGrade(marks)
    d={'name':n,'marks':marks,'grade':grade}
    print(d)
main()
    
    
        
    
