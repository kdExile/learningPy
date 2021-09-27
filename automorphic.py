def automorphic(n):
    square=n*n
    while n>0:
        if n%10!= square%10:
            return False
        n//=10
        square//=10
    return True
def main():
    n=int(input("enter a number"))
    if automorphic(n):
        print(n,"is Automorphic")
    else:
        print(n,"is not Automorphic")
main()
