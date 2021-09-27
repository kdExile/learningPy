def fun(n):
    n=n**2
    print(n)
def fun1(s):
    s=s.upper()
    print(s)
def fun2(l):
    for i in range(len(l)):
        l[i]*=2
    print(l)
def fun3(l1):
    l1=[100,200,300]
    print(l1)
def main():
    n=5
    print(n,"I am in main")
    fun(n)
    print(n,"Back in main")
    s='good morning'
    print(s,"I am in main")
    fun1(s)
    print(s,"Back in main")
    l=[1,2,3]
    print(l,"I am in main")
    fun2(l)
    print(l,"Back in main")
    l1=[10,20,30]
    print(l1,"I am in main")
    fun3(l1)
    print(l1,"Back in main")
main()
    
    
