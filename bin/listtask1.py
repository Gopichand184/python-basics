city_name = ['Bangalore ', 'Kolkata ', 'Chennai', 'Delhi', 'Jammu']
print(type(city_name),"length of city_name is" ,len(city_name))
city_name.remove("Delhi")
print(city_name)
for x in city_name:
  if "indore" in x:
      print("yes indore exists in list ")
  else:
      print("no indore is not in the list")
      break

city_name.extend(["Kanpur","Chandigarh"])
print(city_name)
# for x in city_name:
#     print(x)
a = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []
for i in  a:
    if ( i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)
print("even_list" , even)
print("odd_list" , odd)
dict = dict(zip(odd, even))
print(dict)
print(dict.keys())
print(dict.values())
a =['abc', 'xyz', 'aba', '1221', '2342','samples']
total_length = len(a)
for i in a:
    print(len(i))
      if len(i) > 1 and i[0] == i[-1]:
          print(i)

print(total_length)












