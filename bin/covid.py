import csv
from datetime import datetime
with open("/Users/apple/Downloads/785492_1361825_bundle_archive/covid.csv",'r') as covid:
    reader = csv.reader(covid)
    x = []
    col = []
    for data in reader:
        x.append(data)
    fields = x[0]
    col.append(x[0][1])
    col.append(x[0][2])
    col.append(x[0][3])
    # print(col)
    # print(fields)
    rows = x[1:]
    # dict = dict(zip(x[0],x[1]))
    # print(dict)
    # exit()


    # print(fields)
    # print(rows)
    updated_list = []
for row in rows:
    l = []
    date = datetime.strptime(row[3],'%d-%m-%Y')
    formated_date = date.strftime('%m/%d/%Y')
    # print(formated_date)
    if row[1] == '1':
        row[1] = "male"
    if row[1] == '2':
        row[1] = "female"
    if row[2] == '1':
        row[2] = "positive"
    if row[2] == '2':
        row[2] ="negative"
    row[8] = int(row[8])
    row[9] = int(row[9])
    # print(l)
    l.append(row[1])
    l.append(row[2])
    l.append(row[3])
    l.append(row[8])
    l.append(row[9])
    sum = (row[8]+row[9])
    l.append(sum)

    # print(l)
    # exit()
    updated_list.append(l)
    # print(updated_list)
    # exit()
    # print(row[0],row[1],row[2],row[8])
with open('covid1','w') as c1:
        writer = csv.writer(c1)
        writer.writerow(col)
        writer.writerows(updated_list)
# sex,patient_type,entry_date,diseases,linage
# female,positive,04-05-2020,27,97,124,{"peneumonia":1,"diabates":0},[]
# female,positive,19-03-2020,24,97,121,{"peneumonia":1,"diabates":0},[]
# male,negative,06-04-2020,54,2,56,{"peneumonia":1,"diabates":0},[]
# female,negative,17-04-2020,30,97,127,{"peneumonia":1,"diabates":0},[]
