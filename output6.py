def fun(a=200,b=100,c=5):
    return a+2*b+3*c
def main():
    print(fun(10,20,30))
    print(fun(10,20))
    print(fun(10))
    print(fun())
    print(fun(b=10,a=20,c=30))
main()
