#Caeser Cipher
def CaesarCipher(w):
    t=""
    for ch in w:
        if ch.isalpha():
            if ch.isupper() and ord(ch)<=77 or ch.islower() and ord(ch)<=109:
                t=t+chr(ord(ch)+13)
            else:
                t=t+chr(ord(ch)-13)
        else:
            t+=ch
            
        
        
    return t
def main():
    sent=input("enter a sentence")
    i,c=0,0
    sent=sent+" "
    t=""
    while i<len(sent):
        i=sent.find(' ',i)
        t=t+CaesarCipher(sent[c:i])+" "
        i+=1
        c=i
    print(t)
    sent=t
    t=""
    i,c=0,0
    while i<len(sent):
        i=sent.find(' ',i)
        t=t+CaesarCipher(sent[c:i])+" "
        i+=1
        c=i
    print(t)
main()
    
