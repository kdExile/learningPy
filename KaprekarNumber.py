def main():
    n =int(input("Enter a number"))
    square=n*n
    c=0
    num=n
    while n>0:
        c=c+1
        n=n//10
    if (square//(10**c)+square%(10**c))==num:
        print(num," is a Kaprekar number")
    else:
        print(num," is not a Kaprekar number")
main()
