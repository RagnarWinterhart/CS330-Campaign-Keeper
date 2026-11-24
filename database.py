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
        """
        SELECT id, name, campaign_id, player_id
        FROM player_character
        """,
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
    
def create_session(campaign_id, session_name, session_date, notes):
    return _execute_query(
        """
        INSERT INTO game_sessions(campaign_id, session_name, session_date, notes)
        VALUES (%s, %s, %s, %s)
        """,
        (campaign_id, session_name, session_date, notes),
        return_id=True
    )


def get_sessions():
    return _execute_query(
        "SELECT * FROM game_sessions",
        fetch=True
    )   
    
    
def get_session_character(name, campaign_id):
    results = _execute_query(
        """
        SELECT id FROM player_character
        WHERE name = %s AND campaign_id = %s
        """,
        (name, campaign_id),
        fetch=True
    )

    if len(results) == 1:
        return results[0][0]

    return None

def add_attendance(session_id, character_id):
    return _execute_query(
        """
        INSERT INTO session_attendance(session_id, player_character_id)
        VALUES (%s, %s)
        """,
        (session_id, character_id)
    )


def remove_attendance(session_id, character_id):
    return _execute_query(
        """
        DELETE FROM session_attendance
        WHERE session_id = %s AND player_character_id = %s
        """,
        (session_id, character_id)
    )


def get_session_characters(session_id):
    return _execute_query(
        """
        SELECT pc.id, pc.name
        FROM session_attendance sa
        JOIN player_character pc
            ON sa.player_character_id = pc.id
        WHERE sa.session_id = %s
        """,
        (session_id,),
        fetch=True
    )
          
          
def get_campaign_id_by_name(name):
    results = _execute_query(
        "SELECT id FROM campaign WHERE name = %s",
        (name,),
        fetch=True
    )
    return results[0][0] if len(results) == 1 else None


def get_player_id_by_name(name):
    results = _execute_query(
        "SELECT id FROM player WHERE name = %s",
        (name,),
        fetch=True
    )
    return results[0][0] if len(results) == 1 else None


def get_character_id_by_name(name, campaign_id):
    results = _execute_query(
        """
        SELECT id FROM player_character
        WHERE name = %s AND campaign_id = %s
        """,
        (name, campaign_id),
        fetch=True
    )
    return results[0][0] if len(results) == 1 else None



def get_session_attendance_counts(campaign_name):
    return _execute_query(
        "SELECT gs.id, gs.session_name, COUNT(sa.player_character_id) AS attendance_count " +
        "FROM game_sessions gs JOIN campaign c ON gs.campaign_id = c.id " +
        "LEFT JOIN session_attendance sa ON gs.id = sa.session_id " + 
        "WHERE c.name = %s "  +
        "GROUP BY gs.id, gs.session_name "
        "ORDER BY gs.id;",
        (campaign_name,),
        fetch=True
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