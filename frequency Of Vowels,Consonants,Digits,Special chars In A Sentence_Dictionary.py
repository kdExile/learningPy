def main():
    a=input("enter a sentence")
    v,c,dg,sc=0,0,0,0
    a=a.lower()
    for w in a:
        print(w)
        if w.isalpha():
            if w in 'aeiou':
                v+=1
            else:
                c+=1
        elif w.isdigit():
            dg+=1
        else:
            sc+=1
    d={'vowel':v,'consonant':c,'digit':dg,'special characters':sc}
    print(d)
main()    
