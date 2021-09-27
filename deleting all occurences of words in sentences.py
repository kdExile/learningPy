def main():
    s=input('enter sentence')
    w=input('enter word')
    l=s.split()
    while w in l:
        l.remove(w)
    print(l)
main()
    
