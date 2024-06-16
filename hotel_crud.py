import mysql.connector

#mysql server details
db_connection = mysql.connector.connect(host="localhost",user="root",password="root",database="Hotel_db")

#create a cursor to execute sql queries

cursor=db_connection.cursor()

#create a database

#create_database_query="CREATE DATABASE Hotel_db";
#cursor.execute(create_database_query)

db_connection.commit()

'''#creating table

#table query

#create_table_query="""CREATE TABLE staff(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(56),position VARCHAR(56),salary INT)"""

#query execution

#cursor.execute(create_table_query)
#db_connection.commit()

#insert data into table

insert_data_query="""INSERT INTO staff(name,position, salary) VALUES(%s,%s,%s) """

data_to_insert=[("john","chef",50000),("sami","manager",90000),("rocky","cook",9000)]


cursor.executemany(insert_data_query,data_to_insert)

db_connection.commit()'''



#create 2 nd table

#table 2 query

#create_table_query="""CREATE TABLE booking(booking_id INT AUTO_INCREMENT PRIMARY KEY, guest_id INT, room_num INT,room_price INT)"""

#query execution

#cursor.execute(create_table_query)
#db_connection.commit()

#insert data into table 2

insert_data_query="""INSERT INTO booking(guest_id,room_num,room_price) VALUES(%s,%s,%s) """

data_to_insert=[(23,102,5000),(24,103,4000),(25,104,6000)]


cursor.executemany(insert_data_query,data_to_insert)

db_connection.commit()


