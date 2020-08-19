import pandas as pd
import numpy as np
data = {'Emp_name':['Frank','jessi','Bent','Hardward','smith'],'Emp_id':['1234','2345','3634','1782','3739'],
      'gender':['male','female','male','male','male'],"salary":['20$','47$','35$','45$','37$']}
data1 ={'stu_name':['jack','peter','anna'],'stu_id':['35','67','87'],'stu_marks':['20','30','40']}
df = pd.DataFrame(data,index=[1,2,3,4,5])
df1 = pd.DataFrame(data1,index=[1,2,3])
rows = len(df.axes[0])
columns= len(df.axes[1])
df['rank']= ['a','b','c','d','e']
df['Emp_name']= df['Emp_name'].replace('Frank','harley')
df.pop
print(df)
df.loc['6'] = ['harley','7564','male','50$']
res = df.sort_values(by ='Emp_name')
print(res)
print(df)
print("Total rows is:",rows)
print("Total columns is:",columns)
print(df)
print(df.info())
print(df1)
df2 = pd.concat([df,df1])
print(df2)
print(df.iloc[1])
print(df.head(3))
print(df.iloc[[1,2],[0,3]])
print(df[df['salary']>'20$'])
print(df[df['salary'].between('20$','40$')])
print(df['salary'].sum())
print(df1['stu_marks'].mean())
print(df[['Emp_name','salary']])
x = df2.isnull
x = df2.dropna()
x = df2.fillna('hi')
x = df2.sort_values('Emp_name')
x= df2.count()
x = df.rename(columns={'Emp_name':'EMP_NAME'})
x = df.replace('1','one')
x =list(df.columns.values)
g1 = df.groupby(["Emp_name"]).size().reset_index(name='Number of people')
print(g1)
















# import pandas as pd
# import numpy as np
#
# exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#         'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#         'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#         'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#
# df = pd.DataFrame(exam_data , index=labels)
# print("Summary of the basic information about this DataFrame and its data:")
# print(df.info())