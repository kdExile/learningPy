def squareOfDigits(n):
    s=0
    while n>0:
        s+=(n%10)**2
        n//=10
    return s

def happy(n):
    flag=False
    while n>9:
         if squareOfDigits(n)==1:
            flag=True
            break
         else:
            n=squareOfDigits(n)
    if n==7:
        flag=True
    return flag

def main():
    n=int(input("enter a number"))
    if happy(n):
        print("Happy number")
    else:
        print("Sad number")
main()

   
