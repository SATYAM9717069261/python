import sqlite3

conn = sqlite3.connect(student.db)
print "Opened database successfully";

cursor = conn.execute("SELECT name, marks from Marks")
for row in cursor:
   print "Name = ", row[0]
   print "Marks = ", row[1]
   "\n"
print "Operation done successfully";
conn.execute("UPDATE marks set name = “leesa” where marks = 52")
conn.commit()

cursor = conn.execute("SELECT name, marks from Marks")
for row in cursor:
   print "Name = ", row[0]
   print "Marks = ", row[1]
   "\n"
conn.execute("DELETE from marks where name = “leesa”;")
conn.rollback()
conn.close()
