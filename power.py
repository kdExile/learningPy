def power(a=5,b=2):
    p=1
    for i in range(b):
        p*=a  #p=p*a
    return p


def values(*num):
    for i in num:
        print(i,i**2)
    

def main():
    a=int(input("enter base"))
    y=input("enter y if need power otherwise we will display square of the number")
    if y.upper()=='Y':
        
        b=int(input("enter power"))
        x=power(b=4,a=3)
        print(a,'raised to the power of',b,'is',x)
    else:
        
        x=power(a)
        print("stay happy with your square!",x)
    print(power())
    values(1,2,3,4,5,6,7)
        
    
    
main()
    
