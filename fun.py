import math
'''def fun(n):
    def sad(c):
        return(c)
    return n,sad(n*n)
    print("good bye")'''


def area(r,a):
    aC=math.pi*r*r
    aS=a*a
    return aC,aS

def main():
    '''a=fun(10)
    print(a)
    print(type(a))
    print(fun(5))'''
    r=float(input("enter radius"))
    a=float(input("enter side"))
    areaOfCircle,areaOfSquare=area(r,a)
    if areaOfCircle>areaOfSquare:
        print("area of circle greater")
    elif areaOfCircle<areaOfSquare:
        print("area of square greater")
    else:
        print("equal area")
    
main()

