def vowel(l):
    return "aeiouAEIOU".find(l)!=-1
def main():
    word=input("enter word")
    x=sorted(word,key=vowel,reverse=True)
    print(''.join(x))
main()
    
