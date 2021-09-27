def listFormation(n):
    l=[]
    while n>0:
        l.append(n%10)
        n//=10
    return l
def main():
    n=int(input("enter a number"))
    i=1
    l=listFormation(n)
    flag=True
    while i<7:
        l2=listFormation(n*i)
        for el in l2 :
            if l.count(el)!=l2.count(el):
                flag=False
                break
        if not flag:
            break
        i+=1
         
    if flag:
        print("yes")
    else:
        print("no")
main()
#142857
