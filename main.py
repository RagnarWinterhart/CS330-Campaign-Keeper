from campaign_menu import input_campaign, view_campaigns
from database import (
    create_campaign,
    create_player,
    create_character,
    get_session_attendance_counts
)
from player_character_menu import(
    input_character, 
    input_player, 
    view_characters, 
    view_players
)
from session_menu import(
    create_session_menu,    
    view_sessions
)


# -------------------------
# Main menu
# -------------------------

def display_menu():
    print("\n=== Campaign Keeper ===")
    print("1. View Campaigns")
    print("2. Create Campaign")
    print("3. View Players")
    print("4. Create Player")
    print("5. View Characters")
    print("6. Create Character")
    print("7. View Sessions")
    print("8. Create Session")
    print("9. Session Attendance")
    print("0. Exit")


def main():
    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            view_campaigns()

        elif choice == "2":
            campaign_id = create_campaign(*input_campaign())
            if campaign_id:
                print("Campaign created successfully!")
            else:
                print("Failed to create campaign.")

        elif choice == "3":
            view_players()

        elif choice == "4":
            player_id = create_player(input_player())
            if player_id:
                print("Player created successfully!")
            else:
                print("Failed to create player.")

        elif choice == "5":
            view_characters()

        elif choice == "6":
            character_data = input_character()

            if character_data is not None:
                character_id = create_character(*character_data)

                if character_id:
                    print("Character created successfully!")
                else:
                    print("Failed to create character.")

        elif choice == "7":
            view_sessions()

        elif choice == "8":
            create_session_menu()
            
        elif choice == "9":
            c = input("Enter Campaign name: ").strip()
            attendance = get_session_attendance_counts(c)

            print("\n=== Session Attendance ===")

            if not attendance:
                print("No sessions found for this campaign.")
            else:
                for session in attendance:
                    session_id, session_name, attendance_count = session

                    print(f"\nSession Name: {session_name}")
                    print(f"Characters Attended: {attendance_count}")
                    print("-------------------------")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid selection. Please try again.")

# -------------------------
# Start application
# -------------------------

if __name__ == "__main__":
    main()
