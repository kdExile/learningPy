def pangram(s):
    s=s.lower()
    s=s.replace(' ','')
    t=''
    for ch in s:
        if not ch.isalpha():
            return False
        if t.find(ch)==-1:
            t=t+ch
    print(t)
    return len(t)==26
def main():
    s=input('enter sentence')
    if pangram(s):
        print(s,'is a pangramic sentence')
    else:
        print(s,'is not a pangramic sentence')
main()
