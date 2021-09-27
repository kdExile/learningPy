def recPalindrome(s):
    if len(s)<=1:
        return True
    elif s[0]!=s[-1]:
        return False
    else:
        return recPalindrome(s[1:-1])
def main():
    s=input("enter a word")
    if recPalindrome(s):
        print("Palindrome")
    else:
        print("not a Palindrome")
main()
