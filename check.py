import math
def main():
    print(max(10,5))
    print(max(10.0,5.0))
    print(max(10,5.0))
    print(max([10,20,30,40]))
    print(max(['john','jim','jane']))
    print(max(['john','jim','jane'],['john','jim','robert']))
    #print(max([10,20,30,40],50))
    print(max([10,20,30,40],[10,20,50]))
    print(max((10,20,30,40),(50,)))
    #print(max([10,'good']))
    #print(max([10,20,30,40],(10,20,50)))
    #print(max({1:11,2:22},{1:11,4:44}))
    print(max(10,20,30,40))

    print(sum([10,20,30,40],10.0))
    print(sum((10,20,30,40),50))
    #print(sum(10,5.0))
    print(sum({1:11,2:22}))
    print(max({'ann':25,'jane':15,'tom':5}))
    #print(sum({'ann':25,'jane':15,'tom':5}))
    print(0**0)#1
    #print(math.sqrt(-1))#math domain error
main()


#FOR max() and min()
#mixed datatypes-not comparable(EXCEPTION-int and float)
#list/tuple lexicographically max
#int-float comparable but no auto promotion
#tuples-tuples and list-list comparable and returns the larger 
#dict-dict not comparable
#mixed datatypes within single list or tuple--> not comparable
#when list and list obj are compared, it returns a list object
#when tuple and tuple obj are compared, it returns a tuple object


#sum():---
#cannot add non-iterable obj like int and float
#only on single iterable obj and int/float
#only on single iterable obj but containing numbers only
#can have atmost 2 arguments
#cannot add 2 iterables
#does not act on str obj








