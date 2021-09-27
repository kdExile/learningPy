import random
def main():
    l=int(input("enter lower limit"))
    u=int(input("enter upper limit"))
    n=int(input("enter number of elements"))
    nl=[7, 1, 5, 4, 1, 4, 3, 4, 4, 4,1,1,1]
    #nl=[]
    n=13
    '''for i in range(n):
        nl.append(random.randint(l,u))
    print(nl)'''
    i=0
    while i<len(nl)-1:
        j=i+1
        
        while j<len(nl):
            if nl[i]==nl[j]:
                nl.remove(nl[j])
                i-=1
                break
            j+=1
        i+=1
    print(nl)
        
main()


#never use range() when using remove()
#it is safe to remove 1 at a time
