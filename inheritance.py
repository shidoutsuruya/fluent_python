class hello:
    def __init__(self,*args,**kwargs):
        self._a=5
        self._c=[1,2,3]
    def _hello(self,b):
        self.b=b
    
class world(hello):
    def __init__(self):
        super().__init__()
        self._b=9
    def _hellos(self):
        super()._hello(3)
        
        
    
a=world()
print(a._c)
