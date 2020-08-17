# # named tuple
# from collections import namedtuple
# a = namedtuple('details', 'name, age,study')
# b = a('Gopi chand','23','btech')
# c = a._make(['gopichand','23','btech'])
# print(b)
# print(c)
#
# # deque
# from collections import deque
# a = ['g','o','p','i','c','h','a','n','d']
# b = deque(a)
# b.append('hello')
# b.appendleft('hi')
# b.pop()
# print(b)
#
# # chain map
# from collections import ChainMap
# a = {'fname':'gopi','lname':'chandu'}
# b = {'greet':'hello'}
# Chain_map = ChainMap(a,b)
# d = {'initial':'paladugu'}
# newchain_map = Chain_map.new_child(d)
# print(newchain_map)
#
# # counter
# from collections import Counter
# a = [1,3,2,4,6,23,5,3,7,4,6]
# x = Counter(a)
# print(x)
# print(list(x.elements()))
# print(x.most_common())
# sub ={3:1,4:1}
# print(x.subtract(sub))
# print(x.most_common())
#
# # ordered dict
# from collections import OrderedDict
#
# d = OrderedDict()
# d[1] = 'gopi'
# d[2] = 'chandu'
# d[3] = 'hi'
# d[4] = 'hello'
# print(d)
# d[1] = 'hi'
# print(d)
#
# # default dict
# from collections import defaultdict
#
# d = defaultdict(int)
# d[1] = 'gopi'
# d[2] = 'chandu'
# print(d)
# print(d[3])
#
#
# # exercise questions
# # deque
# a = ["Messi","Ronaldo","Neymar"]
# b = deque(a)
# b.append("carlos")
# b.appendleft("pique")
# b.pop()
# b.count('Messi')
# print(b)
#
# # chainmap
# dict1={'M':1,'I':2,'S':3}
#
# dict2={'E':4,'S':5,'R':6}
#
# chain_map = ChainMap(dict1,dict2)
# print(chain_map.get('R'))
# print(chain_map)
# print(list(chain_map.keys()))
# print(list(chain_map.values()))
# dict3 = {'0':9,'Q':8}
# newchain_map = chain_map.new_child(dict3)
# print(newchain_map)
#
# # namedtuple
# x = namedtuple('details','name,age')
# y1 = x('roberto','34')
# y2 = x('carlos','42')
# y3 = x('micheal','20')
# print(y1._asdict())
# print(y2._asdict())
# print(y3._asdict())

