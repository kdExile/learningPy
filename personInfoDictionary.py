def persons():
    n=int(input("enter number of students"))
    person={}
#method 1
    for i in range(n):
        
        name=input("enter name")
        age=int(input("enter age"))
        hobby=input("enter hobby")
        data={"age":age,"hobby":hobby}
        person[name]=data
    print(person)
    
#method 2    
    name=[]
    hobby=[]
    age=[]
    data=[]
    for i in range(n):
        
        name.append(input("enter name"))
        age.append(int(input("enter age")))
        hobby.append(input("enter hobby"))
        data.append(dict(zip(['age','hobby'],[age[i],hobby[i]])))
        
    person=dict(zip(name,data))
    print(person)
        
persons()

