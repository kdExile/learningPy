#anagram
def main():
    a=input("enter a word")
    b=input("enter another word")
    x=sorted(a)
    y=sorted(b)
    print(x)
    print(y)
    while len(a)>0 and len(a)==len(b):
        b=b.replace(a[0],'')
        a=a.replace(a[0],'')
        
    if len(a)==0 and len(b)==0:
        print("the words are friends")
    else:
        print("the words are enemies")
main()
