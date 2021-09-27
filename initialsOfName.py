def initialsOfName():
    name=input("enter a name")
    name=' '+name.title()
    initials=""
    ct=0
    for i in range(len(name)):
        if name[i-1]==' ':
            initials+=name[i]+'.'
            ct=i
    initials=initials[:-2]+name[name.index(name[ct],ct):]
    
    print("initials of the name:",initials)
initialsOfName()
            
                    
