import pickle
def main():
    n=int(input('enter number of students'))
    f=open('student.dat','wb')
    
    for i in range(n):
        d={}
        d['name']=input('enter name')
        d['term1']=float(input('enter term 1 marks'))
        d['term2']=float(input('enter term 2 marks'))
        d['percentage']=(d['term1']+d['term2'])/2
        pickle.dump(d,f)
    f.close()


    f=open('student.dat','rb+')
    d={}
    try:
        while True:
            x=f.tell()
            d=pickle.load(f)
            print(d)
            choice1=input('are you happy with your term 1 marks(y/n)')
            if choice1.upper()=='N':
                d['term1']=float(input('enter term 1 marks'))

            choice2=input('are you happy with your term 2 marks(y/n)')
            if choice2.upper()=='N':
                d['term2']=float(input('enter term 2 marks'))
            d['percentage']=(d['term1']+d['term2'])/2
            f.seek(x)
            pickle.dump(d,f)
    except EOFError:
        f.close()
    f=open('student.dat','rb')
    d={}
    try:
        while True:
            d=pickle.load(f)
            print(d)
    except EOFError:
        f.close()
main()
    

            
                
            
        
