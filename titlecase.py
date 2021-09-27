def main():
    s=input('enter a sentence')
    l=s.split()
    for i in range(len(l)):
        l[i]=l[i][0].upper()+l[i][1:].lower()
    print(' '.join(l))
main()






             
