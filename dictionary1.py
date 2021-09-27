def main():
    n=int(input("enter number of students"))
    name=[]
    marks=[]
    for i in range(n):
        name.append((input("enter name")))
        marks.append(int(input("enter marks")))
    z=zip(name,marks)
    print(z)
    print(type(z))
    l=list(z)
    print(l)
    t=tuple(l)
    print(t)
    person=dict(zip(name,marks))
    print(person)
#main()

def dictionary():
    d={}
    n=int(input("enter number of students"))
    for i in range(n):
        name=input("enter name")
        marks=int(input("enter marks"))
        d[name]=marks
    print(d)
    d['Mary']=75
    d['Dorothy']=100
    #print(d['Cynthia'])
    if 'Cynthia' in d:
        print(d['Cynthia'])
    else:
        print("not found") 
    print (d)
dictionary()


    

