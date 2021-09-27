def recfactorial(n):
    if n==0:
        return 1
    return n*recfactorial(n-1)
def recsonn(n):
    if n==0:
        return 0
    return n+recsonn(n-1)

def main():
    n=int(input("enter number"))
    print(recfactorial(n))
    print(recsonn(n))
main()
