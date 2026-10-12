"""
Author: Gerard Ortiz
Date: 10/11/2026
Tier Level: Base

Description:
This program creates a database with a tables named tasks where follow up actions can be called. The program can also
update, delete, sort, and display the table and its rows.
"""
# imports the sqlite3 module
import sqlite3

# creates a connection to the database file and returns false if the file is does not exist
def create_connection(db_file):
    try:    
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error:
        #print("database does not exist")
        return None
    
# creates the database and tasks table
def setup_database(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        priority TEXT DEFAULT 'Medium',
        status TEXT DEFAULT 'Pending',
        due_date TEXT,
        project_id INTEGER )
        """
        )
        conn.commit()
        return
    except sqlite3.Error:
        print("SQLite error encountered, database not created")
        return

# takes in the database name, title of task, description, priority status, and due date and adds to the tasks table
def add_task(conn, title, description, priority, due_date):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO tasks (title,description,priority,due_date) VALUES (?,?,?,?)", (title,description,priority,due_date))
        conn.commit()
        task_id = cursor.lastrowid
        return task_id
    except sqlite3.Error:
        return None

# displays all tasks ordered by priority and due date
def get_all_tasks(conn):
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT * FROM tasks ORDER BY priority, due_date"
            )
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error:
        rows = []
        return rows

# returns on the rows in the tasks table with the specified status
def get_tasks_by_status(conn, status):
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT * FROM tasks WHERE status = ?", (status,)
            )
        rows = cursor.fetchall()
        if len(rows) == 0:
            print("...Tasks with status ", "'",status,"'")
        return rows    
    except sqlite3.Error:
        print("...Tasks with status ", "'",status,"'")
        return

# takes in the task id and changes the status with the input from new_status
def update_task_status(conn, task_id, new_status):
    cursor = conn.cursor()
    cursor.execute(
            "UPDATE tasks SET status = ? WHERE id = ?", (new_status,task_id)
            )
    conn.commit()
    if cursor.rowcount > 0:
        return True
    else:
        return False

# deletes the row from the tasks table with the matching task id
def delete_task(conn, task_id):
    cursor = conn.cursor()
    cursor.execute(
            "DELETE FROM tasks WHERE id = ?", (task_id,)
            )
    conn.commit()
    if cursor.rowcount > 0:
        return True
    else:
        return False
    

# display the rows of the tasks table using f-strings 
def display_tasks(rows_in_tasks):
    if len(rows_in_tasks) == 0:
        print("No tasks found.\n")
    else:
        print(f"{'ID':<5}{'Title':<20} {'Description':<30}    {'Priority':<10} {'Status':<10} {'Due Date':<10}")
        print(f"{'-'*4:<5}{'-'*19:<20} {'-'*29:<30}    {'-'*9:<10} {'-'*9:<10} {'-'*9:<10}")
        for rows in rows_in_tasks:
            print(f"{rows[0]:<5}{rows[1]:<20} {rows[2]:<30}    {rows[3]:<10} {rows[4]:<10} {rows[5]:<10}") 
    return

# collects the tasks from the user with user inputs
def collect_task():
    title = input("Task title: ")
    description = input("Task description: ")
    priority = input("Task priority (High/Medium/Low): ")
    due_date = input("Task due date (mm-dd-yyyy): ")
    return title, description, priority, due_date

# calls create connection. if the connection fails prints an error message. 
# setup_database() is called to create the database and table
conn = create_connection("tasks.db")
if conn == None:
    print("Database does not exist")
else:
    setup_database(conn)
    print("\n=== Personal Task & Project Manager ===")

# uses a while loop to and calls collect_task() and add_task() to populate the tasks table
print("\n=== Add Tasks ===")
continue_collect = input("Add tasks (yes/no): ")
while continue_collect == "Yes":
    title, description, priority, due_date = collect_task()
    task_id = add_task(conn, title, description, priority, due_date)
    print("Task added with ID: ", task_id)
    continue_collect = input("\nCheck out another book? (Yes/No): ").strip().title()
else:
    print("\n..No task added")

# calls get_all_tasks and display_tasks() to display the populated table
print("\n=== All Tasks ===")
rows_in_tasks = get_all_tasks(conn)
display_tasks(rows_in_tasks)

# calls get_tasks_by_status to return tasks with Pending status 
# and calls display_tasks() to display the  table
print("\n=== Pending Tasks ===")
status = "Pending"
rows_in_tasks = get_tasks_by_status(conn, status)
display_tasks(rows_in_tasks)

# calls update_task_status() to update a task and prints a confirmation message
id_to_update = int(input("Enter task id to update"))
new_status = input("Enter new status: ")
update = update_task_status(conn, id_to_update, new_status)
if update == True:
    print("Status updated for task ",id_to_update, ": ", new_status)
else:
    print("No tasks updated")

# calls delete_task() to delete a task and prints a confirmation message
id_to_delete = int(input("Enter task id to delete"))
delete = delete_task(conn, id_to_delete)
if delete == True:
    print("Task with id", id_to_delete," is deleted")
else:
    print("No tasks deleted")

# displays the update table
print("\n=== All Tasks ===")
rows_in_tasks = get_all_tasks(conn)
display_tasks(rows_in_tasks)

#ends the connection to the database
conn.close()
