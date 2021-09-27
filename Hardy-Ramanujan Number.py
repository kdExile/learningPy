#Hardy-Ramanujan number
import math

def cubeRoot(n):
    return n **(1/3)

def nearestCubeRoot(n):
    cbrt = cubeRoot(n)
    floor = math.floor(cbrt)
    ceil = math.ceil(cbrt)
    distanceFromFloor = math.fabs(cbrt - floor)
    distanceFromCeil = math.fabs(cbrt - ceil)
    return ceil if distanceFromFloor >= distanceFromCeil else floor

def Ramanujan(n):
    cbrt=nearestCubeRoot(n)
    ct=0
    st=''
    for i in range(1,cbrt+1):
        for j in range(i+1,cbrt+1):
            if i**3+j**3==n:
                ct+=1
                st=st+displayPairs(i,j,n)
    if ct==2:
        print(st)
    return ct==2

def displayPairs(i,j,n):
    return '\n'+str(n)+'='+str(i)+'^3 + '+str(j)+'^3'

def main():
    n=int(input("enter a number"))
    if Ramanujan(n):
        print (n," ramanujan")
    else:
        print (n," not ramanujan")

main()

    


    
