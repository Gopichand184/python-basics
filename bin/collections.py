# x = [x**2 for x in range(0,10)]
# y= [x for x in range(1,20) if x%2==0 ]
# z = [i for i in range(1,101) if int(i**0.5)==i**0.5]
# print(x)
# print(y)
# print(z)
from collections import Counter
list = [1,2,4,23,5,2,5,6,78,2,3,45,6,3,6,7]
x = Counter(list)
print(x)

