import csv
n=int(input("enter number of singers"))
l=[]
f=open('singers.csv','w',newline='')
swriter=csv.writer(f)
header=['NAME','ALBUM']
l.append(header)
for i in range(n):
    singer=input('enter name of singer')
    album=input('enter name of album')
    s=[singer,album]
    l.append(s)
swriter.writerows(l)
f.close()
f=open('singers.csv','r')
sreader=csv.reader(f)
for i in sreader:
    print(i)
f.close()
