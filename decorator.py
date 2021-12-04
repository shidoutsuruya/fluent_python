
import functools
"""
@functools.wrapper:make sure func.__name__=='func' instead of 'wrapper'
"""
#no argument decorator
def uppercase(func):
    @functools.wraps(func)
    def wrapper(): 
        return func().upper()+'hello world'
    return wrapper
def splits(func):
    @functools.wraps(func)
    def wrapper():
        return func().split()
    return wrapper
@splits
@uppercase
def words():
    return 'hello world'
#decorator with arguments
def deco(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        c=func(*args,**kwargs)
        if c>5:
            return True
        else:
            return False
    return wrapper
@deco
def goods(x,y):
    u=x+y
    return u
#decorator arguments
def decodeco(a,b,c):
    def deco(func): 
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            result=func(*args,**kwargs)
            return a*result+b*result+c*result
        return wrapper
    return deco

@decodeco(2,3,4)         
def cal(x,y):
    return x+y
#decorate with class and argument
class mydecorator:
    '''Decorator'''
    def __init__(self,*dargs,**dkwargs):
        self.a=sum(*dargs)#@mydecorator([1,2])
    def __call__(self,func):
        def wrapper(*args, **kwargs):
            result=func(*args, **kwargs)
            return result+self.a
        return wrapper
@mydecorator([1,2])
def hello(a,b,c,d):
    return a+b+c+d

    

    