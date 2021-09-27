def main():
    s=input("enter a sentence")
    l=s.split()
    d={}
    for word in l:
        if word not in d:
            d[word]=l.count(word)
    print(d)
main()

    
        
