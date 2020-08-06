# W1_day1_lab_1_exercise_1
hrs = input("enter hours :")
rate = input(" enter rate :")
print("pay is ",int(hrs)* float(rate))


# W1_day1_lab_1_exercise_2
car_name = input("enter car name ")
price_1 = 5000
price_2 = 10000
price_3 = 30000
avg = ((price_1+price_2+price_3)/3)
print("On an average", car_name,"costs around" ,avg)

# # W1_day1_lab_2_exercise_1
user_input = input("enter file name :")
ex = open("W1-D1-lab2-1.txt",'w')
ex1 = open("W1-D1-lab2-1.txt")
print("The rain in Spain stays mainly on the plain!​Did Eliza get drenched in the rainy plains of Spain?", file = ex)
ex.close()
import csv
with open ("W1-D1-lab2-1.txt",'w') as file_1:
    writer = csv.writer(file_1)
    writer.writerow("The rain in Spain stays mainly on the plain!​Did Eliza get drenched in the rainy plains of Spain?")
with open ("W1-D1-lab2-1.txt",'r') as file_1:
    reader = csv.reader(file_1)

user_input = input("enter file name :")
ex = open("W1-D1-lab2-2.txt",'a')
print("happy 2020!" ,file = ex)
ex.close()
ex = open("W1-D1-lab2-2.txt")
lines = ex.read()
print(lines)

# LAB 3 - Exercise -1

x = 3
y = 5
str1 = "hello"
str2 = "there!"
list1 = [1, 2 ,3]
dict1 = {'the': 100 ,'is':20}
tuple1 = ('Bob', 25,'us')
tuple2 = ('Bala',30,'india')
print("type of x is :",type(x))
print("type of y is :",type(y))
print("type of str1 is :",type(str1))
print("type of str2 is :",type(str2))
print("type of list1 is :",type(list1))
print("type of dict1 is :",type(dict1))
print("type of tuple1 is :",type(tuple1))
print("type of tuple2 is :",type(tuple2))

# LAB 3 - Exercise -2
x = 5
y = float(3)
z = set(list1)
d = list(dict1.items())
print(d)
print("type of y is :",type(y))
print("type of z is :",type(z))

# LAB 3 - Exercise -3
num_1 =1
num_2 =2
num_3 =3
num_4 =4
avg =((num_1+num_2+num_3+num_4)/4)
print("average is :" , avg)

numbers = [1,2,3,4]
print("sum of numbers in the list is :",sum(numbers))

# LAB 3 - Ex 4​
x = 100
y = -90
print(x-(-y))

num_1 = input("enter x value :")
num_2 = input("enter y value:")
intdiff = int(num_1) - int(num_2)
floatdiff =float(num_1)-float(num_2)
print("diiference of integer values is :",intdiff)
print("diiference of integer values is :",floatdiff)

def pay(hrs,rate):
    pay_value = int(hrs)*int(rate)
    return pay_value
x = pay(45,10)
print("pay is :",x)

def pay(hrs,rate):
    pay_value = int(hrs)*int(rate)
    return pay_value
x = pay(45,10)
print("pay is :",x)
def validHeight(cm):
    try:
        cm = float(cm)
        return 100<=cm<=250
    except ValueError :

        return False
x = validHeight("abc")
print(x)


hrs = input("enter hours :")
rate = input("enter rate :")
hrs = float(hrs)
rate = float(rate)

ot_hrs = hrs-40
if(ot_hrs)>0:
    pay = 40*rate +(1.5*rate*ot_hrs)
else:
    pay = rate*hrs
print("pay is :",pay)

hrs = input("enter hours :")
rate = input("enter rate :")

hrs = int(hrs)
rate = int(rate)

ot_hrs = hrs-40
if(ot_hrs)>0:
    pay = (40*rate)+((1.5*rate)*ot_hrs)
else:
    pay = rate*hrs
print("pay is :", pay)










