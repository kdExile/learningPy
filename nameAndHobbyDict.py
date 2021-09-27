def main():
    n=int(input("enter number of persons"))
    d={}
    for i in range(n):
        name=input("enter your name")
        hobby=input("enter your hobby")
        d[name]=hobby
    print(d)
    print(d.keys())
    print(d.values())
    print(d.items())
    for k,v in d.items():
        print(k,v)
    for k in d:
        print(k)
    if 'sophie' in d:
        print(d['sophie'])
    if 'sophie' in d:
        print(d.get('sophie'))
    
    print(d.get('ramu'))
    print(d.get('ramu','who are you?'))
    print(d.get('sophie','who are you?'))
    #print(d.pop('sophie'))
    print(d.popitem())
    #print(d.pop('ramu'))
    print(d.pop('ramu','who are you'))
    print(d)
    
    
    
main()
