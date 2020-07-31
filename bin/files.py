# # file commands
# file = open('python.txt', 'r')
# file = file.read()
# # opens the python file in reading mode
# for each in file:
#     print (each)
# # print every line in python file one by one
# file = file.read(5)
# # reads upto the mentioned charecter and returns as string
# file = open('python.txt', 'w')
# file.write(" hello")
# file.write("how are you")
# # opens the python file in writing mode we can write into the file by using file .write
# file.close()
# # this command closes the opened file
# with open("python.txt") as file:
#     data = file.readlines()
# # read the lines in the file
# for line in data:
#     line.split()
# # splits the line
with open ("demo",'w') as f:
    f.write(" Hi how are you")
    # f.write([ ["11", "22"],["33","44"],["this is files program"]]) f.write not taking as list it only accepting string
    f.write(" \n my name is chandu")
    f.write("\n my age is 23 ")
    f.write ("\n this is apple laptop")
    f.write("\n this is appended line ")
with open ("demo",'r') as f:
        # list = []
        # for data in f:
        #     list.append(data)
        #     print(list)
        #  appends data to the list
        data = f.read()
        print(data)
        for line in data:
            word = line.split()
            # splits each charecter line by line
            print(word)
        with open ("demo1",'w') as f1:
             f1.writelines(data)
             # writes on file data into another file
             with open('demo') as f, open('demo1') as f1:
                 for line1, line2 in zip(f,f1):
                     print(line1+line2)


