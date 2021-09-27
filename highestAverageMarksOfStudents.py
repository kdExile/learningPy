def main():
    n=int(input("enter number of students"))
    names=[]
    marks=[]
    
    for i in range(n):
        names.append(input("enter name of student"))
        m=[]
        for j in range(5):
            m.append(int(input("enter marks")))
        marks.append(tuple(m))
        
    t=tuple(marks)
    n=tuple(names)
    print(n)
    print(t)
    average=[]
    
    for i in range(n):
        average.append(sum(t[i])//5)
        
    tavg=tuple(average)
    print (tavg)
    maximum=max(tavg)
    print(n[tavg.index(maximum)]," has secured the highest average marks which is ",maximum)
main()
    
    
        
            
