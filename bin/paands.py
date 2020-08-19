import pandas as pd
import numpy as np

# n = np.arange(40)
# n.shape= (4,10)
# print(n)
# n1 =np.zeros(3)
# print(n1)

# a = [1,2,3,4,5]
# names = ["anil","chandu","sai","raja","hi"]
# # n = np.random.randn(5)
# a1 = pd.Series(names,index=a)
# print(a1)

# ind =[1,2,3,4,5]
# arr1= [1,2,3,4,5]
# arr2=[6,7,8,9,11]
# s = pd.Series(arr1,index =ind)
# s1 = pd.Series(arr2,index=ind)
# s_add =s.add(s1)
# s_sub = s1.sub(s)
# print(s)
# print(s1)
# print(s_add)
# print(s_sub)
# print('max',s_add.max())
# labels =[1,2,3,4]
data = {'name':["anil",'chandu','sai','raja'],'age':['27','23','25','26'],'id':['1234','5463','2345','1234'],
        'email id':['anil@gmail.com','chandu@gmail.com','sai@gmail.com','raja@gmail.com']}
data1 = {'name':["anil",'chandu','sai','raja'],'age':['27','23','25','26'],'id':['1234','2134','2345','2635'],
        'email id':['anil@gmail.com','chandu@gmail.com','sai@gmail.com','raja@gmail.com']}

df = pd.DataFrame(data,index=[1,2,3,4])
df1 = pd.DataFrame(data1,index=[5,6,7,8])

# print(df['name'])
df['gender'] = ['male','male','male','male']
# del df['age']
# print(df)
# print(df[1:3])
df2 = df.append(df1)
# x = pd.merge(df,df1, on='id')
# print(x)
grp = df.groupby('id')
print(grp.get_group('1234'))
# df2.pop('age')
# print(df2)
# x= df.head(3)
# x = df.isnull
# x = df2.duplicated()
# print(x)
# print(df.loc[3])
# print(df.columns)
# df1 = df.head()
# print(df1)
# print(df.values)
# print(df.describe())
# transpose = df.T
# print(transpose)
# x = df.sort_values(by = "name")
# print(x)

# x = df.at[4,'name']
# print(x)
# # y= df.dtypes
# # print(y)
# df1 = pd.DataFrame({'a': []})
# y = df1.empty
# print(y)