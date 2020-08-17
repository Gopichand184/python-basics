import csv
with open("details" ,'w') as file_1:
    writer = csv.writer(file_1)
    writer.writerow(["name" ,"gender","age","phone" ,"address","email_id" ])
    writer.writerow(["chandu","male","23","9700","tenali","1234@gmail.com"])
    writer.writerow(["anil", "male", "26", "4084", "usa", "anil@gmail.com"])
    writer.writerow(["raja", "male", "25", "6300", "aus", "raja@gmail.com"])
    writer.writerow(["sai", "male", "24", "9052", "vij", "sai@gmail.com"])
    writer.writerow(["chinni", "female", "22", "1111", "hyd", "chinni@gmail.com"])
with open("details",'r') as file_1:
        reader = csv.reader(file_1)
        x = []
        for data in reader:
            x.append(data)
        # print(x)
        col = x[0]
        # x[0].append("changed_phone")
        # x[0].append("changed_address")
        # header = x[0:5]
        f1_rows = x[1:]
        # print(header)
        print(f1_rows)
        # print(col)
with open("details_1" ,'w') as file_2:
    writer = csv.writer(file_2)
    writer.writerow(["name" ,"gender","age","phone" ,"address","studyies" ])
    writer.writerow(["chandu","male","24","1234","bnglr","chandu@gmail.com"])
    writer.writerow(["anil", "male", "27", "4854", "can", "kumar@gmail.com"])
    writer.writerow(["raja", "male", "26", "6476", "usa", "nagaraju@gmail.com"])
    writer.writerow(["sai", "male", "25", "8764", "tnl", "krishna@gmail.com"])
    writer.writerow(["chinni", "female", "23", "1435", "chnn", "ndjfn@gmail.com"])
with open("details_1", 'r') as file_2:
        reader = csv.reader(file_2)
        y = []
        for data in reader:
            y.append(data)
        # print(y)
        fields = y[0]
        # print(fields)
        f2_rows = y[1:]
        # print(rows)
with open("updated", 'w') as updated_file:
    writer = csv.writer(updated_file)
    # writer.writerow(col)
    z = 0
    for i in f1_rows:
        if i != f2_rows[z]:
            updated_file.write(f2_rows[z])
            i = i+1
            print(updated_file)
#



    # x[0].append("changed_phone_no")
    # x[0].append("changed_address")



