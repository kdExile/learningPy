def recSumOfSquaresOfDigits(n):
    if n==0:
        return 0
    return ((n%10)**2)+recSumOfSquaresOfDigits(n//10)


def recHappy(n):
    if n<=9 :
        if n==7 or n==1:
            return 1
        else:
            return 0
    return recHappy(recSumOfSquaresOfDigits(n))

def main():
    n=int(input("enter a number"))
    if recHappy(n)==1:
        print("Happy number")
    else:
        print("Sad number")
        
main()
    
