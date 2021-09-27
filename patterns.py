def main():
    n=int(input("enter number of lines"))
    for i in range(n,0,-1):
        a=97
        for j in range(1,n+1):
            if j<1:
                print('  ',end='')
            else:
                print(chr(a),'',end='')
                a+=1
        print()
main()
