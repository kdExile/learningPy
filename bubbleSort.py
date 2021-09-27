def bubbleSort():
    n=int(input("enter number of elements"))
    a=[]
    for i in range(n):
        a.append(int(input("enter number")))
    counter=0    
    for i in range(n-1):
        flag=False
        for j in range(n-1-i):
            counter+=1
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                flag=True
        if not flag:
            break
        
    print("sorted:",a)
bubbleSort()

