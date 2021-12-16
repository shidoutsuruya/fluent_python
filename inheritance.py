from numba import jit
import functools
import time   
class hello:
    def __init__(self,*args,**kwargs):
        self._a=5
        self._c=[1,2,3]
    def _hello(self):
        return 0
    
class world(hello):
    def __init__(self):
        super().__init__()
        self._b=9
    def _hello(self):
        return 'hello world'
 
 
def times(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time
        start=time.time()
        print(func(*args, **kwargs))
        stop=time.time()
        print('-'*10+'time'+'-'*10)
        print(stop-start)
    return wrapper   


@jit(nopython=True)
def f(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)  
    

