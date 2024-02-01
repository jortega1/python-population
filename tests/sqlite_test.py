import sqlite3
from sqlite3 import Error

# Method for creating connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

# Method for creating table
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

# Method for INSERT projects
def create_project(conn, project):
    sql = ''' INSERT INTO projects(name,begin_date,end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

# Method for INSERT tasks
def create_task(conn, task):
    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

# Method for SELECT all tasks
def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    for row in rows:
        print(row)  

# Method for SELECT all projects
def select_all_projects(conn):  
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = r"new.db"

    # Create a database connection
    conn = create_connection(database)

    # Create table queries
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    # Create tables
    if conn is not None:
        # Create projects table
        create_table(conn, sql_create_projects_table)

        # Create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")
    with conn:
        # Insert project driver code
        # project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
        # project_id = create_project(conn, project)

        # tasks
        # task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
        # task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

        # Create Task Driver Code
        # create_task(conn, task_1)
        # create_task(conn, task_2)

        # Select statements driver code    
        print("Tasks")
        select_all_tasks(conn)
        print("Projects")
        select_all_projects(conn)


if __name__ == '__main__':
    main()