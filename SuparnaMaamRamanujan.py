def SuparnaMaamRamanujan(n):
    c=n
    sm=0
    r=0
    while c>0:
       sm+=c%10
       c//=10
    s=sm
    while sm>0:
        r=r*10+sm%10
        sm//=10
    return s*r==n
def main():
    #n=int(input("enter a number"))
    for n in range(1,10000):
        if SuparnaMaamRamanujan(n):
            print(n,"is misinformed Ramanujan number")
    
    
main()
