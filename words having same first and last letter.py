def main():
    n=int(input("enter number of words"))
    l=[]
    for i in range(n):
        l.append(input("enter a word "))
    for word in l:
        if len(word)>=2 and word[0]==word[-1]:
            print (word)
main()
        
