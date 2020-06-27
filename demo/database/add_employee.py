import sqlite3

con = sqlite3.connect(r"c:\classroom\may25\hr.db")
cur = con.cursor()
name = input("Enter  fullname :")
job = input("Enter job :")
salary = int(input("Enter salary :"))
try:
    cur.execute("insert into employees(fullname,job,salary) values(?,?,?)", (name, job, salary))
    print("Added Successfully!")
    con.commit()
except:
    print("Sorry! Could not add employee due to error!")

con.close()
