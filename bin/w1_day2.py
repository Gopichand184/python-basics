# reversing the tuple
Tuple = (10, 20, 30, 40, 50)
tuple1 = Tuple[::-1]
print(tuple1)

Tuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(Tuple[1][1])

# swapping tuples
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1,tuple2 = tuple2,tuple1
print(tuple1)
print(tuple2)

# copiying elements into another tuple
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:-1]
print(tuple2)

# sorting tuple by position 2
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))

print(tuple1)

tuple1 = (50, 10, 60, 70, 50,60,60)
count = 0
for i in tuple1:
    if i == 50:
        count = count+1
# print(count)

tuple1 = (45, 45, 45, 45)
for i in tuple1:
    if i in tuple1:
        print("true")
    else:
        print("false")

set1= {4,5}
set2= {1,2,3,4,5}
print(set1.issubset(set2))
print(set2.issubset(set1))

set1= {1,2,3,4,5}
set2= {4,5,6,7,8}
set1.update(set2)
print(set1)

set1= {1,2,3,4,5}
set2= {4,5,6,7,8}
set3 = set1.intersection(set2)
print(set3)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict = dict(zip(keys,values))
print(dict)
#
sampleDict = {
      "name": "Kelly",
      "age" : 25,
      "salary": 8000,
      "city": "New york"}
del sampleDict ["name"]
del sampleDict ["salary"]
print(sampleDict)

sampleDict = {'a': 100, 'b': '200', 'c': 300}
for x,y in sampleDict.items():
    if y== 200:
        print("yes 200 exists in sample dictonary")
        exit()
    else:
        print("number not exists")

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"}
sampleDict["location"] = sampleDict["city"]
del sampleDict["city"]
for x,y in sampleDict.items():
    print(x,y)


# sampleDict = { "class":{ "student":{ "name":"Mike", "marks":{ "physics":70, "history":80 } }}}
print(sampleDict['class']['student']['marks']['history'])




