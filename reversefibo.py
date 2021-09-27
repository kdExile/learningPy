def revfibo(n):
    a,b,c=0,1,0
    for i in range(n):
        #print(b)
        c=a+b
        a=b
        b=c
    for j in range(n):
        print (a)
        c=b-a
        b=a
        a=c
def main():
    n=(int)(input("Enter number of terms "))
    revfibo(n)
main()
    
    
