# creating calculator for calculating lcm and hcf for only two numbers
#name:khushi kundwani, class 12 A, IP project, Session 2021-22

import pandas as pd
import mysql.connector as msc
import time


mydb=msc.connect(
    host="localhost",
    user="root",
    password="apple@123",
    auth_plugin="mysql_native_password"
)

crs=mydb.cursor(buffered = True)

q1= "CREATE DATABASE IF NOT EXISTS ipproject"
crs.execute(q1)
q2= "USE ipproject"
crs.execute(q2)
q3= "CREATE TABLE IF NOT EXISTS history(Number1 int(10),Number2 int(10),LCM int(10),HCF int(10) )"
crs.execute(q3)

print("\nCalculator for LCM/HCF\n")
va = 1
value = int(input("For how many pairs you want to calculate?\n"))
while va <= value :
    va = va + 1
    a = input("Type LCM or HCF\n")
    b = a.lower()
    x = int(input("Enter first number:\n"))
    y = int(input("Enter second number:\n"))


    def lcm_finder(x, y):
        L = x if x > y else y
        while L <= x * y:
            if L % x == 0 and L % y == 0:
                return L
            L += 1


    def hcf_finder(x, y):
        n = x if x < y else y
        while n >= 1:
            if x % n == 0 and y % n == 0:
                return n
            n = n - 1

    lc = lcm_finder(x,y)
    hc = hcf_finder(x,y)

    if b == "lcm":
        print("Required LCM is",lc)

    elif b == "hcf":
        print("\nRequired HCF is",hc)
    else:
        print("There was an error\nRestart your program")
        break


crs.execute("INSERT INTO history VALUES (30,45,90,15)")
crs.execute("INSERT INTO history VALUES (153,66,3366,3)")
crs.execute("INSERT INTO history VALUES (15,6,30,3)")
crs.execute("INSERT INTO history VALUES (45,30,90,15)")
crs.execute("INSERT INTO history VALUES (83,69,5727,1)")
crs.execute("INSERT INTO history VALUES (36,69,828,3)")
crs.execute("INSERT INTO history VALUES (30,45,90,15)")
crs.execute("INSERT INTO history VALUES (79,11,869,1)")
crs.execute("INSERT INTO history VALUES (44,11,44,11)")
crs.execute("INSERT INTO history VALUES (11,79,869,1)")
crs.close()
mydb.commit()

time.sleep(2)
print("=============================================\n\t\t\t\tHISTORY TABLE\n=============================================")
df=pd.read_sql("select * from history",mydb)
print(df)

qe = input("Do you want to download HISTORY table\n type YES or NO\n")
qe1 = qe.lower()
if qe1 == "yes":
    print("File is downloaded in Desktop Folder")
    df.to_csv("c:\\users\\khushi\\desktop\\history.csv")
elif qe1 == "no":
    pass
else:
    pass