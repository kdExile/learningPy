import csv
def calcAverage(l):
    return sum(l)/5
def calcGrade(m):
    grade=''
    if m>=90:
        grade='A'
    elif m>=70:
        grade='B'
    elif m>=50:
        grade='C'
    elif m>=30:
        grade='D'
    else:
        grade='E'
    return grade
def main():
    n=int(input('enter number of students'))
    f=open('student result.csv','w',newline='')
    a=csv.writer(f,delimiter='#')
    a.writerow(['name','percentage','grade'])
    for i in range(n):
        l=[]
        l.append(input('enter name of student'))
        p=[]
        for j in range(5):
            p.append(float(input('enter marks')))
        m=calcAverage(p)   
        l.append(str(m))
        l.append(calcGrade(m))
        a.writerow(l)
    f.close()
    f=open('student result.csv','r')
    a=csv.reader(f,delimiter='#')
    c=0
    for i in a:
        #print(i)
        c+=1
        if i[2]>'B' and c>1:
            print(i[0])
    f.close()
main()
    
    
