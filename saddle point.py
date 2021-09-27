#saddle point
def main():
    n=int(input("enter number of rows/columns"))
    r=[]
    for i in range(n):
        c=[]
        for j in range(n):
            c.append(int(input("enter number")))
        r.append(c)
    print(r)
    flag=False
    for i in range(n):
        minimum=min (r[i])
        k=r[i].index(minimum)
        maximum=r[0][k]
        
        for j in range(n):
            if r[j][k]>maximum:
                maximum=r[j][k]
        if minimum==maximum:
            print("saddle point:",minimum)
            flag=True
    if not(flag):
        print("no saddle point")
main()
            
