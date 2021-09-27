def main():
    l1=[1,2,3]
    l2=[4,5,6]
    l3=l1.copy()
    l1.append(l2)
    print(l1)
    l3.extend(l2)
    print(l3)
    a=l3.remove(5)
    print(a,l3)
    b=l1.pop(2)
    print(b,l1)
    c=l3.pop()
    print(c,l3)
    #l2.remove(7)
    del l2[1]
    print(l2)
    l3.clear()
    print(l3)
    del l2
    #print(l2)
    s='abc'
    print(s,type(s))
    l=list(s)
    d=''.join(l)
    print(l,type(l),d,type(d))
    l[0]='d'
    print(l)
    #s[0]='d'
    #print(s)
main()
