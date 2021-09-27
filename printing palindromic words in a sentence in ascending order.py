def isPalindrome(s):
    s=s.lower()
    return s==s[::-1]
def main():
    s=input('enter a sentence')
    l=s.split()
    a=[]
    for i in l:
        if isPalindrome(i):
            a.append(i)
    a.sort()
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if len(a[j])>len(a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    
            
    print(a)
main()
    
