
import pickle
def main():
    '''f=open('personupdate.dat','wb')
    n=int(input('enter number of persons'))
    for i in range(n):
        d={}
        d['name']=input('enter name')
        d['DOB']=input('enter date of birth')
        d['phone']=input('enter phone number')
        pickle.dump(d,f)
    f.close()'''
    '''f=open('personupdate.dat','rb+')
    b=False
    while not b:
        try:
            x=f.tell()
            print(x)
            d=pickle.load(f)
            print(d)
            ch=input('enter Y if your name is incorrect otherwise N')
            if ch.upper()=='Y':
                s=input('enter name again')
                d['name']=s
            f.seek(x)
            pickle.dump(d,f)
        except EOFError as e:
            print(e)
            b=True
        
            f.close()'''
    f=open('personupdate.dat','rb')
    b=False
    while not b:
        print(f.tell())
        try:
        
            d=pickle.load(f)
            print(d)
        except EOFError as e:
            print(e)
            b=True
            
            #f.close()
    #f=open('personupdate.dat','rb')
    f.seek(30,2)
    b=False
    while not b:
        print(f.tell())
        try:
        
            d=pickle.load(f)
            print(d)
        except EOFError as e:
            print(e)
            b=True
            
            f.close()
    
               
            
main()
    
    
    
