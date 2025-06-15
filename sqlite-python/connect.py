# Program to create a new SQLite database
import sqlite3
try:
    with sqlite3.connect("my.db") as conn:
        print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")

except sqlite3.OperationalError as e:
    print("Failed to open database:", e)

# When you pass the literal string ':memory:' to the connect() 
# function of the sqlite3 module, it will create a new database that resides
# in the memory.    
import sqlite3
try:
    with sqlite3.connect(':memory:') as conn:
        # interact with database
        pass
except sqlite3.OperationalError as e:
    print("Failed to open database:", e)

# Creating new tables from Python
import sqlite3

database = '<your_database>'
create_table = '<create_table_statement>'

try:
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        cursor.execute(create_table)   
        conn.commit()

except sqlite3.OperationalError as e:
    print(e)



# CREATE TABLE statements to create the tables:
import sqlite3

sql_statements = [ 
    """CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY, 
            name text NOT NULL, 
            begin_date DATE, 
            end_date DATE
        );""",

    """CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL, 
            priority INT, 
            project_id INT NOT NULL, 
            status_id INT NOT NULL, 
            begin_date DATE NOT NULL, 
            end_date DATE NOT NULL, 
            FOREIGN KEY (project_id) REFERENCES projects (id)
        );"""
]
# create a database connection
try:
    with sqlite3.connect('my.db') as conn:
        # create a cursor
        cursor = conn.cursor()

        # execute statements
        for statement in sql_statements:
            cursor.execute(statement)

        # commit the changes
        conn.commit()

        print("Tables created successfully.")
except sqlite3.OperationalError as e:
    print("Failed to create tables:", e)

'''Use the execute() method of a Cursor object to execute the 
CREATE TABLE statement for creating a new table in the SQLite database file.'''

#inserts data into the projects and tasks tables:
import sqlite3
def add_project(conn, project):
    # insert table statement
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    # Create  a cursor
    cur = conn.cursor()
    # execute the INSERT statement
    cur.execute(sql, project)
    # commit the changes
    conn.commit()
    # get the id of the last inserted row
    return cur.lastrowid
def add_task(conn, task):
    # insert table statement
    sql = '''INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
             VALUES(?,?,?,?,?,?) '''
    # create a cursor
    cur = conn.cursor()
    # execute the INSERT statement
    cur.execute(sql, task)
    # commit the changes
    conn.commit()
    # get the id of the last inserted row
    return cur.lastrowid
def main():
    try:
        with sqlite3.connect('my.db') as conn:
            # add  a project
            project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30')
            project_id = add_project(conn, project)
            print(f'Created a project with the id {project_id}')
            # add tasks to the project 
            tasks = [
                ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02'),
                ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')
            ]
            for task in tasks:
                task_id = add_task(conn, task)
                print(f'Created task with the id {task_id}')
    except sqlite3.Error as e:
        print(e)
if __name__ == '__main__':
    main()

'''Use the execute() statement of the Cursor object to execute 
an INSERT statement to insert a row into a table.
Use the commit() method of the Connection object to apply the 
change to the database permanently.'''

#1) Updating one field of one row in a table
import sqlite3
sql = 'UPDATE tasks SET priority = ? WHERE id = ?'
try:
    with sqlite3.connect('my.db') as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (2,1) )
        conn.commit()
except sqlite3.OperationalError as e:
    print(e)

#2) Updating multiple columns of one row in a table
import sqlite3
sql = 'UPDATE tasks SET priority = ?, status_id = ? WHERE id = ?'
try:
    with sqlite3.connect('my.db') as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (3,2,1) )
        conn.commit()
except sqlite3.OperationalError as e:
    print(e)

#3) Updating multiple columns of multiple rows in a table
import sqlite3
sql = 'UPDATE tasks SET end_date = ?'
try:
    with sqlite3.connect('my.db') as conn:
        cursor = conn.cursor()
        cursor.execute(sql, ('2015-02-03',) )
        conn.commit()
except sqlite3.Error as e:
    print(e) 

'''Use the execute() method of the Cursor object to execute an UPDATE 
statement to update data in a table.'''       

#query 
import sqlite3
conn = sqlite3.connect(database)
cur = conn.cursor()
cur.execute('SELECT * FROM table')
rows = cur.fetchall()
conn.close()
for row in rows:
   print(row)

'''Use the fetchall() method of the cursor object to return all rows of a query.
Use the fetchone() method to return the next row returned by a query.
Use the fetchmany() method to return some rows from a query.'''

#Deleting Data
import sqlite3
sql = 'DELETE FROM tasks WHERE id = ?'
try:
    with sqlite3.connect('my.db') as conn:
        cur = conn.cursor()
        cur.execute(sql, (1,))
        conn.commit()
except sqlite3.OperationalError as e:
    print(e)

'''
Call the execute() method of a Cursor object to run a DELETE 
statement that deletes a row from a table.
Always call the commit() method of the Connection object to permanently 
delete data from a table.
'''    

