import math
def nearestPerfectSquare(n):
    s=int(math.sqrt(n))
    if s*s==n:
        return n
    if n-(s*s)< ((s+1)**2)-n:
        return s*s
    else:
        return (s+1)**2

def main():
    n=int(input("enter number of elements"))
    l=[]
    for i in range(n):
        l.append(int(input("enter number")))
    m=[nearestPerfectSquare(v) for v in l]   
    #m=[(round(math.sqrt(v)))**2 for v in l]
    print(m)
    print(round(15.245673,4))
main()
    
    
