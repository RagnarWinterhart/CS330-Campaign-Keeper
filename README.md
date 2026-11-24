
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

These migration files create and update the tables used by the application. Apply them manually in order; the application does not run migrations automatically.

## Installation and Configuration

1. Clone or download this repository and open a terminal in the project directory.

2. Install the Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your local MySQL connection settings:

   ```env
   DB_HOST=localhost
   DB_USER=your_mysql_username
   DB_PASSWORD=your_mysql_password
   DB_NAME=campaign_keeper
   ```

Replace the example username and password with your own MySQL credentials. Keep `.env` private and do not commit it to version control.

## Running the Application

After setting up the database and `.env` file, run:

```bash
python main.py
```

The terminal menu provides options for managing campaigns, players, characters, sessions, and attendance.

## Project Structure

- `main.py` — starts the application and displays the main menu
- `campaign_menu.py` — campaign-related