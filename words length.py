def main():
    n=int(input("enter length of list"))
    l=[]
    c=0
    for i in range(n):
        l.append(input("enter word"))
    mx=len(l[0])
    mn=len(l[0])
    for i in l:
        if len(i)>mx:
            mx=len(i)
        if len(i)<mn:
            mn=len(i)
    for i in l:
        if len(i)>mn and len(i)<mx:
            print (i)
            c+=1
    if c==0:
        print("all words have same length",l)
    
main()        
