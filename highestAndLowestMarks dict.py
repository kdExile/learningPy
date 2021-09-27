def main():
    n=int(input("enter number of students"))
    l=['roll number','highest','lowest','average marks']
    x=[]
    for i in range(n):
        marks=[]
        data=[]
        for j in range(5):
            marks.append(int(input("enter your marks")))
        data.append(int(input("enter your roll number")))
        data.append(max(marks))
        data.append(min(marks))
        data.append(sum(marks)/5)
        d=dict(zip(l,data))
        x.append(d)
    for i in x:
        for a,b in i.items():
            print (a,b)
    
main()
