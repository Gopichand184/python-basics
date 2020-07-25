print("hello world")
x = 10
print(x)
print(type(x))
y = float(x)
print(y)
print(type(y))
z = complex(x)
print(z)
print(type(z))
a = ("python basics program")
b = ("python \\ basics program")
c = ("python \t basics \t program")
d= ("chandg")
print(d.replace("g", "u"))
print(a)
print(b)
print(c)
print(a.upper())
print(a.lower())
print(a.split())
x = "python" in a
print(x)
x = a +" "+b
print(x)
name = "gopi chand"
age = 24
details = "my name is {} and my age is {}"
print(details.format(name,age))
print(type(a))
a = [1,9,2,7,3,6,4]
b = ["gopi","chand"]
print(sum(a))
print(min(a))
print(max(a))
print(all(a))
print(len(a))
print(sorted(a))
print(reversed(a))
print(a[::-1])
print(a[1:4])
print(a[-5:-1])
print(a[:2])
print(a[2:])
a[1] = "chandu"
a.append("gopi")
a.insert(3,"hi")
del a[4]
a.pop()
a.extend(b)
print(a)
if "gopi" in a:
    print("yes , 'gopi' in this list")
set1 = {"gopi ","chand"}
set2 = {1,2,3,4}
set1.add("anil")
set2.discard(3)
x = set1.union(set2)
print(x)







