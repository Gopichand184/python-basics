import re
# str = 'hi this is gopichand gopi'
# if re.search('gopi',str):
#     print("match found for gopi")
# else:
#     print("no match found ")
# find = re.findall("gopi",str)
# print(find)
#
# for i in re.finditer('gopi',str):
#     res = i.span()
#     print(res)
#
# str1 = "mat,rat,hat,sat"
# res = re.findall("[mrht]at",str1)
# print(res)
#
# reg = re.compile("[r]at")
# bt = reg.sub("bat",str1)
# print(bt)
#
# str3 = "12345 ,123, 1432,5341"
# print("matches:",len(re.findall("\d[3-6]",str3)))

# str1 = "aa ,aab,aabb,aacbc"
# str2 = "cb,cbb,cabbb,cr"
# res = re.findall("[a]b{2}",str1)
# res1 = re.findall("[a]b+",str2)
# res2 = re.findall("b{2,3}",str1)
# print(res)
# print(res1)
# print(res2)

a = 'chandu,sai,an_il,ra_ja'
res = re.findall('[a-z]+_[a-z]+[a-z]',a)
print(res)

b = 'Chandu,Anil,raja,sai'
res = re.findall("[A-Z]+[a-z]",b)
print(res)


str1 = "aa ,aab,aabb,aacbc"
res = re.findall("[a].*?b",str1)
print(res)

str = " hi my name is gopi chand "
print("matches:",len(re.findall('[hi]',str)))