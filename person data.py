import csv
def main():
    n=int(input('enter number of persons'))
    l=[]
    for i in range(n):
        d={}
        d['name']=input('enter name')
        d['DOB']=input('enter date of birth in yyyy/mm/dd format')
        d['phone']=input('enter phone number')
        l.append(d)
    print(l)
    with open('persondata.csv','w',newline='')as f:
        a=csv.writer(f)
        a.writerow(['Name','Date of Birth','Phone number'])
        for j in l:
                   b=list(j.values())
                   a.writerow(b)

    with open('persondata.csv','r')as f:
                   a=csv.reader(f)
                   for i in a:
                       print(i)
                   
                   
                   
        
    
main()
    
