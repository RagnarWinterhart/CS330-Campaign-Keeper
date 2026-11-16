CREATE DATABASE IF NOT EXISTS campaign_keeper;
USE campaign_keeper;
SHOW TABLES;
SHOW CREATE TABLE player_character;

CREATE TABLE IF NOT EXISTS campaign(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20),
    game_system varchar(20),
    description text

);

CREATE TABLE IF NOT EXISTS player(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name varchar(50)
);
CREATE TABLE IF NOT EXISTS player_character(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    campaign_id INTEGER NOT NULL,
    player_id INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,

    FOREIGN KEY (campaign_id) REFERENCES campaign(id),
    FOREIGN KEY (player_id) REFERENCES player(id)
);
