
import sqlite3

con = sqlite3.connect(r"c:\classroom\may25\hr.db")
cur = con.cursor()
id = int(input("Enter employee id :"))
salary = int(input("Enter new salary :"))
cur.execute("update employees set salary = ? where empid = ?", (salary,id))
if cur.rowcount == 1:
    print("Updated Successfully!")
    con.commit()
else:
    print("Sorry! Employee id not found!")

con.close()
