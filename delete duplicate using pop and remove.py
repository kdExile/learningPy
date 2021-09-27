def delDuplicateUsingRemove(l):
    i=0
    while i<len(l):
        t=l[i+1:]
        
        while len(t)>0 and t.count(l[i])>0:
            t.remove(l[i])
        l=l[:i+1]+t
        i+=1
        
    print(l)
    return(l)

def delDuplicateUsingPop(l):
    i=0
    while i<len(l):
        j=i+1
        while j<len(l):
            if l[i]==l[j]:
                l.pop(j)
                j-=1
            j+=1
        i+=1
    print(l)

def delDuplicate(l):
    i=0
    #n=len(l)
    while i<len(l):#i<n
        j=i+1
        x=j
        while j<len(l):#j<n
            if l[i]!=l[j]:
                l[x]=l[j]
                x+=1
            j+=1
        l=l[:x]#n=x
        i+=1
    print(l)#l[:n]

def reverse1(l):
    return l[::-1]

def reverse2(x):
    l=list(x)
    for i in range(len(l)//2):
        l[i],l[len(l)-i-1]=l[len(l)-i-1],l[i]
    return l


            
    
 
def main():
    l1=[2]
    l2=[2,2]
    l3=[2,1,2,1]
    l4=[1,0,2,3,4]
    l5=[1,2,4,1,4,3]
    '''delDuplicateUsingRemove(l1)
    delDuplicateUsingRemove(l2)
    delDuplicateUsingRemove(l3)
    delDuplicateUsingRemove(l4)
    delDuplicateUsingRemove(l5)
    delDuplicateUsingPop(l1)
    delDuplicateUsingPop(l2)
    delDuplicateUsingPop(l3)
    delDuplicateUsingPop(l4)
    delDuplicateUsingPop(l5)'''
    '''delDuplicate(l1)
    delDuplicate(l2)
    delDuplicate(l3)
    delDuplicate(l4)
    delDuplicate(l5)'''
    
    l=[1,2,3,4,5,6,7,8,9]
    print(reverse1(l))
    
    print(reverse2(l))
    
    reverse2(l).reverse()
    
    print(l)
    
main()


#shallow copying:x=l, the same memory address is assigned and refers to the same list
#deep copying:x=list(l), another object is created and a new memory address is assigned





