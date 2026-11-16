USE campaign_keeper;

CREATE TABLE IF NOT EXISTS game_sessions(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    campaign_id INTEGER NOT NULL,
    session_name VARCHAR(50),
    session_date DATE,
    notes TEXT,
    FOREIGN KEY (campaign_id) REFERENCES campaign(id)
);

CREATE TABLE IF NOT EXISTS session_attendance(
    session_id INTEGER NOT NULL,
    player_character_id INTEGER NOT NULL,
    PRIMARY KEY (session_id, player_character_id),
    FOREIGN KEY (session_id) REFERENCES game_sessions(id),
    FOREIGN KEY (player_character_id) REFERENCES player_character(id)
);
