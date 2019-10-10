import sqlite3
conn = sqlite3.connect('student7.db')
def create_table():
    conn.execute('''CREATE TABLE marks
         (
         NAME           TEXT    NOT NULL,
         MARKS            INT     NOT NULL );''')
    print "Table created successfully";

def insert():
    conn.execute("INSERT INTO marks (NAME,MARKS) \
      VALUES ('Satyam',100 )");
    conn.execute("INSERT INTO marks (NAME,MARKS) \
      VALUES ( 'Umair', 25 )");
    conn.commit()
    print "Records created successfully";
   

def select():
    cursor = conn.execute("SELECT NAME,MARKS from marks")
    for row in cursor:
        print "Name =" ,row[0];
        print "Marks = ", row[1], "\n" ;

def update():
    conn.execute("UPDATE marks SET NAME='SATYAM MANDAL' WHERE NAME = 'Satyam' " );

def delete(i_d):
    conn.execute("DELETE FROM marks where NAME='{}'".format(i_d) );

create_table();
insert();
select();
update();
select();
delete(raw_input("Enter Student id =>") );
select();
