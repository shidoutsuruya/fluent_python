from collections import ChainMap,Counter
'''test chainmap'''
a={'python':5,'java':3,'c++':1}
b={'ruby':4,'python':9}
chain=ChainMap(a,b)
#print(chain['python'])
'''test counters'''
string='aaaaadsadsadasdsa'
ct=Counter(string)
print(ct)
ct.update('abce')
u=a.keys()|{'hello'}
print(u)