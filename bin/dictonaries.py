dict = {"name": "chandu", "age" : "24", "colour" : "black"}

for x in dict.values():
    print(x)
for x in dict.keys():
    print(x)
for x in dict :
    print(x)
for x,y in dict.items():
    print(x,y)
print(len(dict))
x = dict.get("name")
print(x)
dict["colour"] = "white"
print(dict)
dict.pop("colour")
print(dict)

