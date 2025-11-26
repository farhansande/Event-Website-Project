import mysql.connector

## Will use this to connect to the SQL/functions that require me to access SQL


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="@County0",
        database="data"          
    )

def insert_user(username: str, password: str):
    conn = get_connection()
    cursor = conn.cursor()

    if getUserID(username) is not None:
        return "Username already exists"
    sql = """
    INSERT INTO user (Username, Password)
    VALUES (%s, %s)
    """

    cursor.execute(sql, (username, password))
    conn.commit()

    cursor.close()
    conn.close()

def getAllUsers():
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT *
    FROM user
    """

    cursor.execute(sql)
    
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

def getUser(id):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT *
    FROM user
    WHERE UserID = %s
    """

    cursor.execute(sql, (id, ))
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row is None:
        return None
    
    return row

def update_user(user_id: int, new_username: str, new_password: str): 
    conn = get_connection()
    cursor = conn.cursor()

    if getUserID(new_username) is not None: # As it only checks if the new username exists, it handles the issue of only the username being changed.
        return "Username already exists"

    sql = """
    UPDATE user
    SET Username = %s, Password = %s
    WHERE UserID = %s
    """

    cursor.execute(sql, (new_username, new_password, user_id))
    conn.commit()

    cursor.close()
    conn.close()

def loginUser(username: str, password: str): # User login logic
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = """
    SELECT Username, Password
    FROM user
    WHERE Username = %s AND Password = %s
    """

    cursor.execute(sql, (username, password))
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row is None:
        return None
    
    return getUserID(username)

def getUserID(username):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT UserID
    FROM user
    WHERE Username = %s
    """

    cursor.execute(sql, (username, ))
    row = cursor.fetchone() # Gets one

    cursor.close()
    conn.close()

    if row is None:
        return None
    
    return row[0]

def remove_user(id: int):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    DELETE FROM user 
    WHERE UserID = %s
    """

    cursor.execute(sql, (id,))
    conn.commit()

    rows_deleted = cursor.rowcount

    cursor.close()
    conn.close()

    return rows_deleted

def insert_event(name: str, time:str, location:str, description:str):
    conn = get_connection()
    cursor = conn.cursor()

    if getEventID(name) is not None:
        return "Event already exists"

    sql = """
    INSERT INTO event (EventName, EventTime, EventLocation, EventDescription)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (name, time, location, description))
    conn.commit()

    cursor.close()
    conn.close()

def update_event(id: int, name: str, time: str, location: str, description: str):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    UPDATE event
    SET EventName = %s, EventTime = %s, EventLocation = %s, EventDescription = %s
    WHERE EventID = %s
    """

    cursor.execute(sql, (name, time, location, description, id))
    conn.commit()

    cursor.close()
    conn.close()

def getEventID(name):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    SELECT EventID
    FROM event
    WHERE EventName = %s
    """

    cursor.execute(sql, (name, ))
    row = cursor.fetchone() # Gets one

    cursor.close()
    conn.close()

    if row is None:
        return None
    
    return row[0]

def delete_event(id: int):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    DELETE FROM event 
    WHERE EventID = %s
    """

    cursor.execute(sql, (id,))
    conn.commit()
    
    rows_deleted = cursor.rowcount

    cursor.close()
    conn.close()

    return rows_deleted

def getAllEvents():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)  # <-- Important: return dicts instead of tuples

    sql = "SELECT * FROM event"
    cursor.execute(sql)
    rows = cursor.fetchall()  # now each row is a dict

    cursor.close()
    conn.close()
    return rows


def getEvent(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM event WHERE EventID = %s"
    cursor.execute(sql, (id,))
    row = cursor.fetchone()  # now a dict
    cursor.close()
    conn.close()
    return row

