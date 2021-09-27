import math
def area(a,b,c):
    s=(a+b+c)/2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

def distance(a,b):
    l1=list(a.values())
    l2=list(b.values())
    return math.sqrt((l1[0]-l2[0])**2+(l1[1]-l2[1])**2)
    
def check(a,b,c):
    return a+b>c and a+c>b and b+c>a
    

def main():
    n=int(input('enter number of co-ordinates'))
    l=[]
    for i in range(n):
          d={}
          d['x']=int(input('enter x coordinate'))
          d['y']=int(input('enter y coordinate'))
          l.append(d)
    print(l)
    b=False
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                a=distance(l[i],l[j])
                b=distance(l[k],l[j])
                c=distance(l[i],l[k])
                print(a,b,c)
                if check (a,b,c):
                    print('TRIANGLE CAN BE FORMED')
                    print('area=',area(a,b,c))
                    b=True
                
    if not b:
        print('no TRIANGLEs could BE FORMED')
        
    
main()
