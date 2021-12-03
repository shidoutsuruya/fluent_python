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
    
    