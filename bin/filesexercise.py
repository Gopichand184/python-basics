# import csv
# with open("demofile" ,'w', ) as f:
#     writer = csv.writer(f)
#     writer.writerows([["12","15"],["2","3"],["my name is anil"]])
#     writer.writerow(["my age is 23","cse"])
#     writer.writerow(["This is apple laptop","mac book"])
# with open("demofile" ,'r') as f:
#     reader = csv.reader(f)
#
#     pass
# # list =[]
# # for data in f:
# #     list.append(data)
# # print(list)
#     with open('demo1','w') as f1:
#         f1.writelines(f)

import csv

with open("/Users/apple/Downloads/785492_1361825_bundle_archive/covid.csv",'r') as covid:
    reader = csv.reader(covid)
    x = []
    for data in reader:
        x.append(data)
    fields = x[0]
    rows = x[1:]
    print(fields)
    print(rows)
    updated_list =[]
    for row in rows:
        # print(row[1],row[2])
        if row[1]=='1':
            row[1] ="male"
        if row[1]=='2' :
            row[1]="female"
        updated_list.append(row)
    with open('covid1', 'w') as c1:
        writer = csv.writer(c1)
        writer.writerow(fields)
        writer.writerows(updated_list)





