import pickle
n=int(input('enter number of movies'))
with open ('movies.dat','wb') as f:
    for i in range(n):
        l=[]
        l.append(input('enter name of movie'))
        l.append(input('enter name of director'))
        pickle.dump(l,f)
    
with open ('movies.dat','rb') as f:
    try:
        for i in range(n):
            l=pickle.load(f)
            print(l)
    except:
        print('END')


    
    
