import random
def main():
    '''n=int(input("enter number of books"))
    d={}
    for i in range(n):
        l=[]
        name=input("enter name of book")
        l.append(input("enter ISBN number"))
        l.append(input("enter name of author"))
        l.append(float(input("enter price")))
        d[name]=l
    print(d)
    book_name=input("enter name of book")
    if book_name in d:
        print(d[book_name])
    else:
        print("Perhaps you have written this book!")'''
    
    '''print('###'.join('HI'))
    l=[1,2,3]
    l.append(range(1,11,3))
    print(l)
    l.extend(range(1,11,3))
    print(l)
    l.extend([1])
    print(l)
    x=1,
    print(type(x))
    l=[1,2,3]
    m=['a','b','c']
    print(max(l),min(l),sum(l))
    print(max(m),min(m))
    #print(sum(m))
    l.extend(m)
    #print(max(l))
    print(sum(l))'''

    '''cards=['diamond','club','heart','spade']
    number=random.randint(0,3)
    for i in range(3):
       
        card_type=input("enter card type")
        if card_type==cards[number]:
            print("you have won!")
            break
        else:
            print("you have lost!")
            
    
    else: 
       print("the correct one is",cards[number]) '''
    x=random.randrange(1,11,3)
    print(x)
    a={1:10,2:20}
    b={2:200,3:300}
    for x in b:
        a[x]=b[x]
    print(a)
    b[3]=3000
    a.update(b)
    print(a)
        
main()
