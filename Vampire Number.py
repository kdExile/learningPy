import math
    
def digitCheck(i,j,n):
    n=str(n)
    i=str(i)
    j=str(j)
    i+=(j)

    if len(i)!=len(n):
        return False
    for k in range(len(n)):
        if  n.count(i[k])!=i.count(i[k]) :
            return False
    return True
                                  
def numberOfDigits(n):
    return ((int)(math.log(n,10)))+1

def Vampire(n):
    dig=numberOfDigits(n)
    d=dig//2
    #print((int)(10**(d-1)),(int)(10**d)-1)
    for i in range((int)(10**(d-1)),(int)(10**d)):#int(math.sqrt(n))
        if n%i==0:
            if digitCheck(i,n//i,n):
                return True,i,n//i
    return False,0,0
            
def main():
    n=13078260
    
    f,x,y=Vampire(n)
    if f:
        print('Vampire',x,y)
    else:
        print("not Vampire")
main()
              













    





'''ex:1260=21*60
    153000 = 300×510'''
    
