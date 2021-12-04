import collections
import math
card=collections.namedtuple('card',['rank','suit'])
class FrenchDeck:
    ranks=[str(n) for n in range(2,11)]+list('JQKA')
    suits='spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards=[card(rank,suit) for rank in self.ranks for suit in self.suits]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self,position):
        return self._cards[position]
    def __contains__(self,item):#item in []
        if item in self._cards:
            print('yes')
            return True
        else:
            print('no')
            return False
    
        
class Vector:
    def __init__(self,x=0,y=0):
        x:int
        y:int
        reference:str
        self.x=x
        self.y=y
    def __repr__(self):
        return f'Vector({self.x},{self.y})'
    def __abs__(self):
        return math.hypot(self.x,self.y)
    def __bool__(self):
        return bool(abs(self))
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)
    def __mul__(self,const):
        return Vector(self.x*const,self.y*const)
    def __sub__(self,other):
        x=self.x-other.x
        y=self.y-other.y
        return Vector(x,y)
    def __truediv__(self,const):
        return Vector(self.x/const,self.y/const)
    def __floordiv__(self,const):
        return Vector(self.x//const,self.y//const)
    def __matmul__(self,other):
        return self.x*other.x+self.y*other.y
    def __lt__(self,other):
        return self.x<other.x and self.y<other.y
