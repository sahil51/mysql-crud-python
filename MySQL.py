############################################################
# CRUD - CREATE, READ, UPDATE AND DELETE #
############################################################


# STEP 1: Connect to MySQL Database

import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Your_Password',
        database='sqql'   #your_database name
    )
cursor=connection.cursor()
print('connection established')

# STEP 2: Create a Database
try:
    cursor.execute('CREATE DATABASE sqql')
    connection.commit()
    print('database created successfully')
except:
    print('having problem to created database')

# STEP 3: Create a Table
cursor.execute(
            '''CREATE TABLE IF NOT EXISTS practice(
                id INT PRIMARY KEY NOT NULL AUTO_INCREMENT UNIQUE,
                name VARCHAR(60),
                age VARCHAR(60),
                contact VARCHAR(60)
            )'''
        )
print('table created successfully')
    
# STEP 4: Show All Tables in Database
cursor.execute('SHOW TABLES')
data = cursor.fetchall()
for x in data:
    print(x)


# STEP 5: Insert New Records Into the Table
cursor.execute('''INSERT INTO practice
               (name,age,contact)
               values
               ("sahil","22","7404304607"),
               ("monu","21","74324304607"),
               ("megha","17","74041565416607")
               ''')
print('data insert in database')
connection.commit()

# STEP 6: Read: Select Data From a Table
cursor.execute('SELECT * FROM practice')
data = cursor.fetchall()
print(data)

# table print in Rows
cursor.execute('SELECT * FROM  practice')
acnt = cursor.fetchall()
for x in acnt:
    print(x)

# STEP 7: Update: Update Data in a Table
cursor.execute('UPDATE practice SET name="yash" WHERE id="2"')
connection.commit()
print('updated')

# STEP 8: Delete Data From a Table
cursor.execute('DELETE FROM practice WHERE id="12"')
connection.commit()
print(cursor.rowcount,'delete successful')

# STEP 9: Truncate Data From a Table
cursor.execute('TRUNCATE TABLE practice')
connection.commit()
print('all data delete successful')




