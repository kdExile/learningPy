def main():
    n=input("Enter a letter/special character/number ")
    a=ord(n)
    if a>=65 and a<=90:
        print ("uppercase letter")
    elif a>=97 and a<=122:
        print ("Lowercase letter")
    elif a>=48 and a<=57:
        print("Number")
    else:
        print ("Special Character")
main()

    
