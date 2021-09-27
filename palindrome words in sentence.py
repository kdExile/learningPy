import math
def check():
    print(math.sqrt(2))
    print(2**0.5)
#check()
def palindrome(w):
    w=w.lower()
    t=''
    for ch in w:
        t=ch+t
    return t==w
def main():
    s=input("enter sentence")
    s=s+' '
    c=0
    i=0
    while i<len(s):
        i=s.find(' ',i)
        word=s[c:i]
        if palindrome(word):
            print (word)
        i+=1
        c=i
main()
