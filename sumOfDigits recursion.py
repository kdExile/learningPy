def sumOfDigits(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s

def recsumOfDigits(n):
    if n==0:
        return 0
    return n%10+recsumOfDigits(n//10)

def recArmstrongNumber(n):
    if n==0:
        return 0
    return recArmstrongNumber(n//10)+((n%10)**3)

def recCountDigits(n):
    if n//10==0:
        return 1
    return 1+recCountDigits(n//10)

def recNarcississticNumber(n,c):
    if n==0:
        return 0
    return recNarcississticNumber(n//10,c)+((n%10)**c)

def recDisariumNumber(n):
    if n==0:
        return 0
    return recDisariumNumber(n//10)+((n%10)**recCountDigits(n))



def main():
    n=int(input("enter number"))
    print(sumOfDigits(n))
    print(recsumOfDigits(n))
    if n<100 or n>999:
        print("go home")
    else:
        print(recArmstrongNumber(n))
        if n==recArmstrongNumber(n):
            print("Armstrong")
        else:
            print("not Armstrong")
            
    if recNarcississticNumber(n,recCountDigits(n))==n:
        print("Narcississtic Number")
    else:
        print("not a Narcississtic Number")
        
    if recDisariumNumber(n)==n:
        print("Disarium Number")
    else:
        print("not a Disarium Number")
        
main()
