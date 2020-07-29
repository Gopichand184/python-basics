# file commands

file = open('python.txt', 'r')
file = file.read()
# opens the python file in reading mode
for each in file:
    print (each)
# print every line in python file one by one
file = file.read(5)
# reads upto the mentioned charecter and returns as string
file = open('python.txt', 'w')
file.write(" hello")
file.write("how are you")
# opens the python file in writing mode we can write into the file by using file .write
file.close()
# this command closes the opened file
with open("python.txt") as file:
    data = file.readlines()
# read the lines in the file
for line in data:
    line.split()
# splits the line

f = open('demofile','w')
f.write("this is chandu")
f.write("my age is 23")
print(f.readline())








