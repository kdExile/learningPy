import random
def hcf(m,n):
    while m>0:
        n,m=m,n%m
    return n

def find(l,el):
    for i in range(len(l)):
        if l[i]==el:
            return True
    return False

def main():
    #n=int(input("enter number of elements "))
    l=[]
    n=50
    for i in range(n):
        x=random.randint(2,100)
        if x not in l:
            l.append(x)
    print(l)
    #l=[2,4,3,1,7,8,5,8,1,3,5,7,9]
    #l=[1,2,3,4,5,6,7,8,9]
    l=[15, 16, 61, 11, 5, 43, 98, 4, 91, 69, 48, 19, 85, 76, 93, 38, 53, 78, 20, 7, 3, 12, 32, 40, 64, 39, 87, 42, 86, 26, 60, 47, 21, 31, 9, 100, 17, 28, 50, 30, 51]
    n=len(l)
    b=[]
    z=[]
    for i in range(n-1):
        v=[]
        v.append(l[i])
        
        for j in range(n):
            x=0
            for k in range(len(v)):
                if hcf(v[k],l[j])==1 and find(v,l[j])==False:
                    x+=1
            if x==len(v):
                v.append(l[j])

        b.append(v)
        z.append(len(v))
    #for i in range(len(b)):
        #print(b[i])
    for i in range(len(b)):
        if len(b[i])==max(z):
            print(b[i])
        
    
main()



