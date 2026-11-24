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
    return _execute_query(
                "SELECT * FROM campaign",
                fetch=True
            )
                
def create_campaign(name, game_system, description):
    return _execute_query(
        "INSERT INTO campaign(name, game_system, description) VALUES " + 
        "(%s, %s, %s)", (name, game_system, description),
        return_id=True
    )
                
def create_player(name):
    return _execute_query(
        "INSERT INTO player(name) VALUES " + 
        "(%s)", (name,),
        return_id=True
    )
                
def get_players():
    return _execute_query(
            "SELECT * FROM player",
            fetch=True
        )
            
def create_character(name, campaign_id, player_id):
    return _execute_query(
        "INSERT INTO player_character(name, campaign_id, player_id) VALUES " + 
        "(%s, %s, %s)", (name, campaign_id, player_id),
        return_id=True
    )
                
def get_characters():
    return _execute_query(
        "SELECT * FROM player_character",
        fetch=True
    )
            
def update_campaign(campaign_id, name, game_system, description):
    return _execute_query(
        "UPDATE campaign SET name = %s, game_system = %s, description = %s WHERE id = %s", 
        (name, game_system, description, campaign_id)
    )


# Probably wont be used, but is here for completeness 
def update_player(player_id, name):
    return _execute_query(
        "UPDATE player SET name = %s WHERE id = %s", (name, player_id)
    )
                
def update_character(character_id, player_id, campaign_id, name):
    return _execute_query(
        "UPDATE player_character SET name = %s, player_id = %s, campaign_id = %s WHERE id = %s", 
        (name, player_id, campaign_id, character_id)
    )
    
    
def delete_character(character_id):
    return _execute_query(
        "DELETE FROM player_character WHERE id = %s",
        (character_id,),
    )

def delete_player(player_id):
    return _execute_query(
        "DELETE FROM player WHERE id = %s",
        (player_id,),
    )

def delete_campaign(campaign_id):
    return _execute_query(
        "DELETE FROM campaign WHERE id = %s",
        (campaign_id,),
    )
                
def _execute_query(query, params=(), fetch=False, return_id=False):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, params)

        if fetch:
            return cursor.fetchall()

        connection.commit()

        if return_id:
            return cursor.lastrowid

        return cursor.rowcount

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()