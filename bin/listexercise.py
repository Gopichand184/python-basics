list = [1,2,3,4]
tot = 1
for x in list:
     tot *= x
print("multiply of list is" ,tot)
x = sum(list)
print("sum of list is ",x)
max = list[0]
for i in list:
    if i > max:
        max = i
print("maximum element in the list is ",max)
min = list[-1]
for i in list:
    if i < min:
        min= i
print("minimum element of the list is " , min)
y = list.copy()
print("copied list is ",y)
list = [1,2,3,4]
for i in list:
    if (i % 2 == 0):
        list.remove(i)
print(list)
# list1 = ["gopi" ," ","chandu"]
# res = list(filter(None, list1))
# print(res)









