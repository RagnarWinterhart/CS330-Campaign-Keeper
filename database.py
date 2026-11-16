import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
def get_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
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
        if connection is not None and connection.is_connected():
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
                
def create_player(name):
    connection = None
    cursor = None
    try: 
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO player(name) VALUES " + 
                        "(%s)", (name,))
        connection.commit()
        return cursor.lastrowid

    finally: 
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
                connection.close()
                
def get_players():
    connection = None
    cursor = None
    try: 
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM player")
        
        records = cursor.fetchall()
        return records
    finally: 
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            
def create_character(name, campaign_id, player_id):
    connection = None
    cursor = None
    try: 
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO player_character(name, campaign_id, player_id) VALUES " + 
                        "(%s, %s, %s)", (name, campaign_id, player_id))
        connection.commit()
        return cursor.lastrowid

    finally: 
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
                connection.close()
                
def get_characters():
    connection = None
    cursor = None
    try: 
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM player_character")
        
        records = cursor.fetchall()
        return records
    finally: 
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            
def update_campaign(campaign_id, name, game_system, description):
    connection = None
    cursor = None
    try: 
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE campaign SET name = %s, game_system = %s, description = %s WHERE id = %s", (name, game_system, description, campaign_id))
        connection.commit()
        return cursor.rowcount

    finally: 
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
                connection.close()


# Probably wont be used, but is here for completeness 
def update_player(player_id, name):
    connection = None
    cursor = None
    try: 
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE player SET name = %s WHERE id = %s", (name, player_id))
        connection.commit()
        return cursor.rowcount

    finally: 
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
                connection.close()
                
def update_character(character_id, player_id, campaign_id, name):
    connection = None
    cursor = None
    try: 
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("UPDATE player_character SET name = %s, player_id = %s, campaign_id = %s WHERE id = %s", (name, player_id, campaign_id, character_id))
        connection.commit()
        return cursor.rowcount

    finally: 
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
                connection.close()