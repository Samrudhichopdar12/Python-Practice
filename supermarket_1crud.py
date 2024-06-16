import mysql.connector


#mysql server details

db_connection = mysql.connector.connect(host="localhost",user="root",password="root",database="Super_Market")

#create a cursor to execute sql queries

cursor=db_connection.cursor()

#create a database

#create_database_query="CREATE DATABASE Super_Market";
#cursor.execute(create_database_query)





#creating table


#table query

#create_table_query= """ CREATE TABLE product(id  INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(56) ,category VARCHAR(56), price INT )"""

#query execution

#cursor.execute(create_table_query)
#db_connection.commit()



#INSERT data into table

insert_data_query = """
INSERT INTO product(name, category,price) VALUES (%s, %s,%s)
"""
data_to_insert = ("rice","grocery",200 )

cursor.execute(insert_data_query, data_to_insert)

db_connection.commit()






