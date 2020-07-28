import random
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
random.shuffle(color)
print("shuffled list is", color)
list = [100, 200, 300, 400, 500]
rev_list = list[::-1]
print("reverse list is" ,rev_list)
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = [i + j for i, j in zip(list1,list2)]
print(result)
list = [100, 200, 300, 400, 500]
print([i*i for i in list])
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)