import itertools
import operator
def iter_count():
    for i in itertools.count(5,5):#*see the iter count function
        if i==35:
            break
        else:
            print(i,end='')
            
def iter_cycle():
    count=0
    for i in itertools.cycle('AB'):
        if count > 7:
            break
        else:
            print(i, end = " ")
            count += 1
#permutation
def cartesian_product():
    print('combination:')
    print(list(itertools.product(['A','B','C'],repeat=3)))
    print('combination with replacement:')
    print(list(itertools.combinations_with_replacement(['A','B','C'],r=3)))
    print('permutation:')
    print(list(itertools.permutations(['A','B','C'],r=3)))
def iter_accumulator():
    ls=range(1,5)
    def func(x,y):
        return x+y
    print(list(itertools.accumulate(ls,operator.mul)))
    print(list(itertools.accumulate(ls,operator.add)))
    print(list(itertools.accumulate(ls,func)))
def iter_chain():
    a=[1,2,3]
    b=[4,5,6]
    c=[7,8,9]
    new=list(itertools.chain(a,b,c))
    print(new)
print (list(itertools.compress('GEEKSFORGEEKS',[1,1,1])))