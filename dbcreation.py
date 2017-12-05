# import sqlite3

# def dbconvertion():

#     values_to_insert = [('1',"foo"), ('2', "bar"), ('3', "baz")]
#     my_list = ['manikandan','ravi','shaker','achnataya','ritka']



#     # name = os.getcwd()+"/static/db/device.sql"



#     name = "/home/manikandan/workspace/driver/static/db/device.sql"
#     conn = sqlite3.connect(name)

#     db = conn.cursor()
#     create_table_sql = """CREATE TABLE IF NOT EXISTS projects(id integer PRIMARY KEY,usn text NOT NULL,qp_data text NOT NULL);"""
#     # sql_record_tables =  """INSERT INTO projects(name) VALUES ('Cardinal');"""
    
#     my_list = [('''INSERT INTO projects(usn,qp_data) VALUES ('%s','%s');''')%(i[0],i[1]) for i in values_to_insert]
    
#     # import ipdb;ipdb.set_trace()
#     db.execute(create_table_sql)
#     # db.execute(sql_record_tables)
#     for item in my_list:
#          db.execute(item)

#     db.execute("SELECT * FROM projects")
#     print(db.fetchall())

#     # c.executemany("""INSERT INTO projects (name) VALUES (?)""", values_to_insert)
#     # c.execute(sql_record_tables)
#     conn.commit()





# dbconvertion()





import sqlite3
import time

def dbconvertion():
    name = "/home/manikandan/workspace/driver/static/md/device.sql"
    conn = sqlite3.connect(name)
    db = conn.cursor()
    create_table_sql = """CREATE TABLE IF NOT EXISTS STUDENT(id integer PRIMARY KEY,
        usn text NOT NULL,passcode text NOT NULL,fp_data text NOT NULL,name text NOT NULL,degree text NOT NULL,
        image text NOT NULL,college text NOT NULL,university text NOT NULL,exam_subject text NOT NULL,
        exam_date datetime default current_timestamp,exam_duration text NOT NULL,
        exam_login_time TIMESTAMP  DEFAULT CURRENT_TIMESTAMP,exam_logout_time DEFAULT CURRENT_TIMESTAMP,
        roll_no text NOT NULL);"""
    # my_list = [('''INSERT INTO projects(usn,qp_data) VALUES ('%s','%s');''')%(i[0],i[1]) for i in values_to_insert]
    db.execute(create_table_sql)
    # for item in my_list:
    #      db.execute(item)
    db.execute("SELECT * FROM STUDENT")
    print(db.fetchall())
    conn.commit()

dbconvertion()













