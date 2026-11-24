
from database import (
    create_campaign,
    get_campaigns,
    update_campaign,
    create_player,
    get_players,
    create_character,
    get_characters,
    update_character
)

def display_menu():
    print("\n=== Campaign Keeper ===")
    print("1. View Campaigns")
    print("2. Create Campaign")
    print("3. View Players")
    print("4. Create Player")
    print("5. View Characters")
    print("6. Create Character")
    print("0. Exit")
    
def main():
    while True:
        display_menu()

        choice = input("Select an option: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            pass
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()