def prime(num):
    f=0
    flag=False
    for i in range(num):
        if (num%(i+1))==0:
            f=f+1
    if f==2:
        flag=True
    return flag
def Goldbach(n):
    for i in range(1,n+1):
        if prime(i)and prime(n-i):
            return True,i,n-i
    return False,0,0
def main():
    n=int(input('enter number of elements'))
    l=[]
    for i in range(n):
        l.append(int(input('enter a number')))
    print(l)
    f=False
    for i in range(n):
        x,y,z=Goldbach(l[i])
        if x:
            print(l[i],'=',y,'+',z)
            f=True
    if not f:
        print('no Goldbach numbers in list')
main()
