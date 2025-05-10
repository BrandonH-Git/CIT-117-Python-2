# Programmer: Brandon Hodgdon
# Project: SQL Database Interaction
# Class: Python Programming 2 - CIT-117
# Date: 9MAY2025

import sqlite3
import csv

#Make the database and connect to it
dbConnection = sqlite3.connect("SocSecPayMin.db")
dbCursor     = dbConnection.cursor()

#Create the 3 tables
dbConnection.execute("CREATE TABLE IF NOT EXISTS Employee(EmployeeID int, Name text)")

dbConnection.execute("CREATE TABLE IF NOT EXISTS Pay(EmployeeID int, Year int, Earnings real)")

dbConnection.execute("CREATE TABLE IF NOT EXISTS SocialSecurityMin(Year int, Minimum real)")


#Loop that reads the employee txt files and puts it into a SQL string statement and executes/commits
sInsertEmployee = "INSERT INTO Employee(EmployeeID, Name) VALUES("
sInsertEmployeeReset = sInsertEmployee

with open("Employee.txt", "r") as file:
      iEmployeeRow = 0
      reader = csv.reader(file)
      next(reader)

      for row in reader:
            sInsertEmployee += f"{row[0]}, '{row[1]}')"
            try:
                dbConnection.execute(sInsertEmployee)
                iEmployeeRow += 1
            except sqlite3.OperationalError:
                print("Could not insert")
            sInsertEmployee = sInsertEmployeeReset
      dbConnection.commit()

#Loop that reads the Pay txt files and puts it into a SQL string statement and executes/commits
sInsertPay = "INSERT INTO Pay(EmployeeID, Year, Earnings) VALUES("
sInsertPayReset = sInsertPay

with open("Pay.txt", "r") as file:
      iPayRow = 0
      reader = csv.reader(file)
      next(reader)

      for row in reader:
            sInsertPay += f"{row[0]}, '{row[1]}', '{row[2]}')"
            try:
                dbConnection.execute(sInsertPay)
                iPayRow += 1
            except sqlite3.OperationalError:
                print("Could not insert")
            sInsertPay = sInsertPayReset
      dbConnection.commit()

#Loop that reads the SocialSecurityMinimum txt files and puts it into a SQL string statement and executes/commits
sInsertSocialSecurityMin = "INSERT INTO SocialSecurityMin(Year, Minimum) VALUES("
sInsertSocialSecurityMinReset = sInsertSocialSecurityMin

with open("SocialSecurityMinimum.txt", "r") as file:
    iSocSecMin = 0
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        sInsertSocialSecurityMin += f"{row[0]}, '{row[1]}')"
        try:
            dbConnection.execute(sInsertSocialSecurityMin)
            iSocSecMin += 1
        except sqlite3.OperationalError:
            print("Could not insert")
        sInsertSocialSecurityMin = sInsertSocialSecurityMinReset
    dbConnection.commit()

#Data reporting that selects the columns, joins the tables, and outputs the selected data
dbCursor.execute("""
SELECT a.Name, b.Year, b.Earnings, c.Minimum
FROM Employee As a
JOIN Pay AS b ON a.EmployeeID = b.EmployeeID
JOIN SocialSecurityMin AS C ON b.Year = c.Year
ORDER BY a.EmployeeID DESC
""")

print(f"{'Employee Name':<20} {'Year':<5} {'Earnings':>15} {'Min':>15} {'Include':>15}")
for row in dbCursor.fetchall():
    fResult = ""
    if row[2] >= row[-1]:
        fResult = "Yes"
    else:
        fResult = "No"
    print(f"{row[0]:<20} {row[1]:<5} {row[2]:>15,.2f} {row[3]:>15,.2f} {fResult:>15}")

#Closing the connection to the database
dbConnection.close()


