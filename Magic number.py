def sumOfDigits(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s
def magic(n):
    flag=False
    while n>9:
         if sumOfDigits(n)==1:
            flag=True
            break
         else:
            n=sumOfDigits(n)
    if n==1:
        flag=True
    return flag
def main():
    n=int(input("enter a number"))
    if magic(n):
        print("Magic number")
    else:
        print("not a Magic number")
main()
