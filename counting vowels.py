def count(s):
    c=0
    for l in s:
        if l in 'aeiouAEIOU':
            c+=1
    return c
def main():
    l=['fly','education','cat','food','rainbow']
    print(sorted(l,key=count))
    
    s='hahahahahahaw'
    print(s.lstrip('ha'))
    
    l=[2,3,4,2,1,5,9,3,5,9,5]
    print(sorted(set(l)))
    
    l[4:6]=['one','five']#the list slice is replaced by the list given on the right side of assignment operator

    l[1:3]=['good','bad','better']
    l[:2]=['happy']
    #in above 2 cases, the list assignment is accomodated even though the slices may be less or more and elements are replaced accordingly
    print(l)
    
main()

'''key:can be used in both sort() and sorted()
        a method name is provided as the value of the key parameter according to which the list is sorted.

lstrip()/rstrip():the given string is stripped from the left or right not only as the all possible combinations
of the parameter but also all the occurences are removed even though the frequency of the letters may be less
in the parameter

set():it removes all duplicates from the list.A set must contain unique elements.'''

