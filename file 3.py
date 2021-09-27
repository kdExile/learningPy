import pickle
def main():
    
    f=open('file.dat','wb')
    d={'name':'John Smith','age':18,'hobby':'reading','occupation':'Student'}
    
    pickle.dump(d,f)
    d={'name':'james bond','age':54,'hobby':'reading','occupation':'Student'}
    pickle.dump(d,f)
    d={'name':'emily bronte','age':25,'hobby':'reading','occupation':'Student'}
    pickle.dump(d,f)
    

    
    f.close()
    x={}
    f=open('file.dat','rb')
    b=True
    
        
    try:
        while b:
            x=pickle.load(f)
            print(x)
    except EOFError:
        f.close()
        print(b)
        
main()
        
    
    
