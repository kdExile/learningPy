def calc(n,m):
    max_marks=max(m)
    s=''
    for i in range(len(n)):
        if m[i]==max_marks:
            s=s+n[i]+'\n'
    return max_marks,s
def main():
    n=int(input("enter number of students"))
    name=[]
    marks=[]
    for i in range(n):
        name.append(input("enter name"))
        marks.append(int(input("enter marks")))
    
    max_marks,top_name=calc(name,marks)
    print("highest marks:",max_marks)
    print("topper(s):",top_name)
main()
