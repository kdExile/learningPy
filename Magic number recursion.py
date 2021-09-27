def recSumOfDigits(n):
    if n==0:
        return 0
    return n%10+recSumOfDigits(n//10)

def recMagic(n):
    if n<=9 :
        if n==1:
            return 1
        else:
            return 0
    return recMagic(recSumOfDigits(n))

def main():
    n=int(input("enter a number"))
    if recMagic(n)==1:
        print("Magic number")
    else:
        print("not a Magic number")
        
main()
    
