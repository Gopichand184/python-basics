list_1 = [1,2,4,5,6,7,8,4,6]
list_2 = ["gopi" ," chandu"]
list_4 = [1,4,6,4,6,5]
list_1.append("184")
# inserts element at the end of the list
print(list_1)
list_3 = list_1.copy()
# copies list and stores in another variable
print(list_3)
y = list_1.count(6)
print("the count of 6 in list is ",y)
# counts how many times item present in the list
list_1.extend(list_2)
print(list_1)
# list_2 will be add to list_1
list_1.insert(1,"hi")
print(list_1)
# inserts element at the mentioned index in the list
list_1.pop()
print(list_1)
# removes element at the end of the list
list_4.sort()
print(list_4)
# prints list in ascending order
print(list_4[1:3])
# prints list in the given indexes
print(list_4[-3:-1])

