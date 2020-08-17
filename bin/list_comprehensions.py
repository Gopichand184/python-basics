# x = [x for x in range(10)]
# y = [x for x in range(1,20) if x%2==0]
# z = [x if x%2==0 else x+1 for x in range(10)]
# print(x)
# print(y)
# print(z)
#
# li = ['chndu', 'gopi','hi','hello']
# x = [x[1] for x in li]
# y = [x.upper() for x in li]
# print(x)
# print(y)
# a = [1,2,3,4,5]
# b = [5,4,3,2,1]
# c = [x+y for x,y in zip(a,b)]
# print(c)
#
# # lamda.map,reduce functions
# from functools import reduce
# a = [1,2,3,4,5,6]
# b = [1,2,3,4,5,6]
# li = ['chndu', 'gopi','hi','hello']
# x = list(map(lambda x :x[0] ,li ))
# even = list(filter(lambda x : x%2==0,a))
# square = list(map(lambda x :x**2,a))
# add  = list(map(lambda x,y :x+y,a,b))
# red = reduce(lambda x,y :x+y ,a)
# print(even)
# print(square)
# print(add)
# print(red)
# print(x)


