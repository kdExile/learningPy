import csv
def main():
    '''n=int(input('enter number of countries'))
    l=[]
    for i in range(n):
        m=[]
    
        m.append(input("enter country"))
        m.append(input("enter capital"))
        m.append(input("enter currency"))
        m.append(input("enter language"))
        l.append(m)
    f=open('countries.csv','w')#newline=''
    a=csv.writer(f)
    a.writerows(l)
    f.close()'''
    f=open('countries.csv','r',newline='\r\n')
    a=csv.reader(f)
    for i in a:
        print(i)
    f.close()
main()
