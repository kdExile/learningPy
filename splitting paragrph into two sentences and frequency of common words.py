def validSentences(s):
    flag=True
    if s.find('.')==-1 and s.find('?')==-1 and s.find('!')==-1:
        flag=False
    if s[--1]=='.' or s[-1]=='?' or s[-1]=='!':
        flag=True
    else:
        flag=False
    return flag
def sentenceSplit(s):
    s=s[:-1]
    st=''
    if s.find('!')!=-1:
        st=s.split('!')
    if s.find('.')!=-1:
        st=s.split('.')
    if s.find('?')!=-1:
        st=s.split('?')
    return st
def commonWordsAndFrequency(s):
    s1=s[0]
    s2=s[1]
    l1=s1.split()
    l2=s2.split()
    flag2=0
    for i in range(len(l1)):
        flag=False
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                flag=True
                break
        if flag:
            print(l1[i], (l2.count(l1[i])+l1.count(l1[i])))
            flag2=1
            l1[i]=''
            l2[j]=''
    if flag2!=1:
        print("no common words")
    
def main():
    s=input("enter paragraph")
    if validSentences(s):
        commonWordsAndFrequency(sentenceSplit(s))
    if not validSentences(s):
        print("invalid input")
    
main()



        
