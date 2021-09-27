p=[]
def rec(l,i):
    n=list(l)
    if i==(len(n)-1):
        return p
    for j in range(len(n)):
        n[i],n[j]=n[j],n[i]
        p.append(''.join(n))
    return rec(n,i+1)

def main():
    n=input('enter a word')
    q=rec(n,0)
    print(len(q))
    for i in range(len(q)):
        print(q[i],end=' ')
        
main()
