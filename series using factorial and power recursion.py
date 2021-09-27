def recFactorial(n):
    if n==0:
        return 1
    return n*recFactorial(n-1)
def recPower(a,b):
    if b==0:
        return 1
    return a*recPower(a,b-1)
def main():
    n=int(input("enter number of terms"))
    x=float(input("enter value of x"))
    s=0
    for i in range(n):
        print(recPower(x,2*i+1),recFactorial(2*i))
        s+=recPower(x,2*i+1)+recFactorial(2*i)
    print("sum of series:",s)
main()
        
