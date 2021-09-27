#Insertion Sort
def main():
    n=int(input("enter number of elements"))
    a=[]
    
    for i in range(n):
        a.append(int(input("enter number")))    

    i=1
    while i<n:
        t=a[i]
        j=i-1
        while j>=0 and a[j]>t:
            a[j+1]=a[j]
            j-=1    
        a[j+1]=t
        i+=1
        
    print("sorted array:",a)

#Fibonacci
    a=0
    b=1
    for i in range(11):
        print(a)
        a,b=b,a+b

    
main()
                
                
        
        
    
