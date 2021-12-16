#from functools import partial,partialmethod,cmp_to_key,reduce,total_ordering,lru_cache,singledispatch,
#* this is tesing functools in python
import functools
print(dir(functools))
class Demo:
    def __init__(self):
        pass
    def add(self,a,b):
        return a+b 
    add_a=partialmethod(add,b=5)
    def __call__(self,x,y):
        print('call call call')
        return x,y
  
# function to sort according to last character
def cmp_fun(a, b):
    if a[-2] > b[-2]:
        return 1
    elif a[-2] < b[-2]:
        return -1
    else:
        return 0
  
#list1 = ['China','Afri','America']
#l = sorted(list1, key = cmp_to_key(cmp_fun))

def try_reduce():
    lst=[4,6,8,8,9,2]
    a=reduce(lambda a,b:a+b,lst)
    return a

@total_ordering
class N:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
  
    # Reverse the function of 
    # '<' operator and accordingly
    # other rich comparison operators
    # due to total_ordering decorator
    def __lt__(self, other):
        return self.value > other.value
@lru_cache(maxsize = None)
def factorial(n):
    if n<2:
        return 1
    return factorial(n-2)+factorial(n-1)

#*differenct action to differnt type
import numpy as np
@singledispatch
def fun(s:str):
    print('hello world:',s)
@fun.register(float)
def _(a,b):
    print(a**2+b)
@fun.register(list)
def _(lst):
    print(sum(lst))
@fun.register(np.ndarray)
def _(ndarray):
    print(np.mean(ndarray))
fun(np.array([1,2,3,4]))
