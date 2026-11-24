# Campaign Keeper

Campaign Keeper is a Python command-line application for organizing tabletop RPG campaigns, players, characters, and game sessions. It uses a MySQL relational database to store campaign information and track which characters attend each session.

## Features

- Create, view, edit, and delete campaigns
- Create, view, edit, and delete players
- Create, view, edit, and delete characters
- Associate characters with campaigns and players
- Create and view game sessions for campaigns
- Add or remove characters from a session's attendance list
- View attendance counts for sessions in a selected campaign

## Technologies

- Python
- MySQL
- `mysql-connector-python` for database access
- `python-dotenv` for loading database configuration from environment variables

## Database Setup

Campaign Keeper uses a local MySQL database named `campaign_keeper`.

1. Create the database in MySQL:

   ```sql
   CREATE DATABASE campaign_keeper;
   ```

2. Apply the SQL migration files in order:

   - `001_initial_schema.sql`
   - `002_expand_campaign_name.sql`
   - `003_game_sessions_table.sql`

   These migrations create and update the tables used by the application.

## Installation and Configuration

1. Clone or download this repository and open a terminal in the project directory.

2. Install the Python dependencies:

   ```bash
   python -m pip install mysql-connector-python python-dotenv
   ```

3. Create a `.env` file in the project root with your local MySQL connection settings:

   ```env
   DB_HOST=localhost
   DB_USER=your_mysql_username
   DB_PASSWORD=your_mysql_password
   DB_NAME=campaign_keeper
   ```

   Replace the example username and password with your own MySQL credentials. Keep `.env` private; do not commit it to version control.

## Running the Application

After setting up the database and `.env` file, run:

```bash
python main.py
```

The terminal menu provides options for managing campaigns, players, characters, sessions, and attendance.

## Project Structure

- `main.py` — command-line menu, user input, and application workflow
- `database.py` — database connection, SQL queries, and CRUD functions
- `migrations/` — SQL files used to create and update the database schema

## Data Model

The database contains the following main tables:

- `campaign` — campaign name, game system, and description
- `player` — player names
- `player_character` — characters associated with a campaign and player
- `game_sessions` — sessions associated with a campaign
- `session_attendance` — records which characters attended each session

A campaign can have multiple characters and sessions. Session attendance connects game sessions and characters, allowing a character to be recorded as attending a session.
