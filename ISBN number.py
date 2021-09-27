#ISBN number
def isISBN(num):
    if len(num)>10 or len(num)<10:
        return False
    for i in range(len(num)-1):
        if not(num[i].isdigit()):
            return False
    if num[-1].isdigit() or num[-1]=='X':
        return True
    else:
        return False
    
def isValid(num):
    return len(num)==10 and num[:9].isdigit() and (num[-1].isdigit() or num[-1]=='X')


def main():
    n=input("enter a number")
    s=0
    if isValid(n):
        for i in range(9):
            s+=(ord(n[i])-48)*(10-i)
        if n[9].isdigit():
            s+=(ord(n[9])-48)
        else:
            s+=ord(n[9])-78
        
        if s%11==0:
            print(n,"is an ISBN number")
        else:
            print(n,"is not an ISBN number")
main()

    
