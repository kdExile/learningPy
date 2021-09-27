def main():
    n=int(input("enter number of countries"))
    countries=[]
    for i in range(n):
        countries.append(input("enter name of country"))
    l=len(countries[0])
    s=len(countries[0])
    for i in range(1,n):
        if len(countries[i])>l:
            l=len(countries[i])
        if len(countries[i])<s:
            s=len(countries[i])
    print("countries with longest name:")
    for i in range(n):
        if len(countries[i])==l:
            print(countries[i])
    print("countries with shortest name:")
    for i in range(n):
        if len(countries[i])==s:
            print(countries[i])
main()
