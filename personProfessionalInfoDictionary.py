def main():
    n=int(input("enter number of persons"))
    person={}

    for i in range(n):
        
        name=input("enter name")
        age=int(input("enter age"))
        profession=input("enter profession")
        salary=int(input("enter salary"))
        data={"age":age,"profession":profession,"salary":salary}
        person[name]=data
    print(person)
main()
