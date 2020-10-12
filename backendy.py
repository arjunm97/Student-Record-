import sqlite3
import pandas as pd

def connect():
    conn=sqlite3.connect("records.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS record(usn integer,name text,subject text,attendence integer,ev1 integer,ev2 integer,ev3 integer,ev4 integer,ev5 integer)")
    conn.commit()
    conn.close()

def insert(usn,name,subject,attendence,ev1,ev2,ev3,ev4,ev5):
    print("inserting")
    conn=sqlite3.connect("records.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO record VALUES(?,?,?,?,?,?,?,?,?)",(usn,name,subject,attendence,ev1,ev2,ev3,ev4,ev5))
    conn.commit()
    conn.close()

def view():
    print("View command")
    conn=sqlite3.connect("records.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM record")
    rows=cur.fetchall()
    conn.close()
    print(rows)
    return rows

def search(name="",usn=""):
    print("seraching")
    conn=sqlite3.connect("records.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM record WHERE name=? OR usn=?",(name,usn))
    r=cur.fetchall()
    conn.close()
    print(r)
    return r

def delete(usn):
    print("deleting")
    conn=sqlite3.connect("records.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM record WHERE usn=?",(usn,))
    conn.commit()
    conn.close()

def update(usn,name,subject,attendence,ev1,ev2,ev3,ev4,ev5):
    print("updating")
    conn=sqlite3.connect("records.db")
    cur=conn.cursor()
    cur.execute("UPDATE record SET usn=?,name=?,subject=?,attendence=?,ev1=?,ev2=?,ev3=?,ev4=?,ev5=? WHERE usn=?;",(usn,name,subject,attendence,ev1,ev2,ev3,ev4,ev5,usn))
    conn.commit()
    conn.close()

def csv ():
     con=sqlite3.connect("records.db")
     query='select * from record'
     data=pd.read_sql(query,con)
     data.to_csv('export.csv')
     con.close()

connect()
'''#insert(2,"arjun","ds",100,10,10,10,10,10)
#view()
#delete("01")
update(2,"june","ds",80,10,10,10,10,10)
view()
search(usn=2)
'''
