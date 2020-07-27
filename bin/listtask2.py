a = [10,20,30,20,10,50,60,40,80,50,40]
a = list(dict.fromkeys(a))
print(a)
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(0)
color.pop(4)
color.pop(3)
for i in color:
    print(i)
list1 = [1, 3, 5, 7, 9]
list2 = [1, 2, 4, 6, 7, 8]
list3 = (list(set(list1) - set(list2)))
print(list3)
list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
list1.append(list2)
print(list1)


print("list task 2")



