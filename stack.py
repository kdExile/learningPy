def empty(l):
    return len(l)==0
def peek(l):
    if empty(l):
        print('Stack underflow')
    else:
        print(l[-1])
def push(l,el):
    l.append(el)
def pop(l):
    if empty(l):
        return 'underflow'
    else:
        return l.pop()
def display(l):
    if empty(l):
        print('underflow')
    else:
        for i in range(len(l)-1,-1,-1):
            print(l[i])

def main():
    l=[]
    while True:
        choice=int(input('enter your choice:1-push,2-pop,3-display,4-peek and 5 for exit'))
        if choice==1:
            n=int(input('enter a number'))
            push(l,n)
        elif choice==2:
            x=pop(l)
            if x=='underflow':
                print('Underflow')
            else:
                print('popped value:',x)
        elif choice==3:
            display(l)
        elif choice==4:
            peek(l)
        elif choice==5:
            break
        else:
            print('Learn to count one to five!!')
main()
            
            
                        
        
    
