import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="campaign_keeper"
        )
    return connection

def get_campaigns():
    connection = None
    cursor = None
    try: 
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM campaign")
        
        records = cursor.fetchall()
        return records
    finally: 
        if cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
                connection.close()
                
def create_campaign(name, game_system, description):
    connection = None
    cursor = None
    try: 
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO campaign(name, game_system, description) VALUES " + 
                        "(%s, %s, %s)", (name, game_system, description))
        connection.commit()
        return cursor.lastrowid

    finally: 
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
                connection.close()