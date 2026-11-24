from database import (
delete_character, 
delete_player, 
get_campaign_id_by_name, 
get_campaigns, 
get_character_id_by_name, 
get_characters, 
get_player_id_by_name, 
get_players, 
update_character, 
update_player)
# -------------------------
# Player functions
# -------------------------

def view_players():
    while True:
        players = get_players()

        print("\n=== Players ===")

        if not players:
            print("No players found.")
        else:
            for player in players:
                print(f"\nName: {player[1]}")
                print("--------------------")

        print("\nE. Edit Player")
        print("D. Delete Player")
        print("0. Back to Main Menu")

        choice = input("Select an option: ").lower()

        if choice == "e":
            edit_player()
        elif choice == "d":
            delete_player_menu()
        elif choice == "0":
            break
        else:
            print("Invalid selection.")


def input_player():
    name = input("Enter a player name: ").strip()
    return name


def edit_player():
    name = input("Enter the player name to edit: ").strip()
    player_id = get_player_id_by_name(name)

    if player_id is None:
        print("Player not found or name is not unique.")
        return

    player = next(
        (p for p in get_players() if p[0] == player_id),
        None
    )

    new_name = input(f"Name [{player[1]}]: ") or player[1]

    result = update_player(player_id, new_name)

    if result:
        print("Player updated successfully.")
    else:
        print("No records were changed.")


def delete_player_menu():
    name = input("Enter the player name to delete: ").strip()
    player_id = get_player_id_by_name(name)

    if player_id is None:
        print("Player not found or name is not unique.")
        return

    confirmation = input(
        f"Delete player '{name}'? (y/n): "
    ).lower()

    if confirmation == "y":
        try:
            result = delete_player(player_id)

            if result:
                print("Player deleted successfully.")
            else:
                print("Player not found.")

        except Exception as error:
            print(f"Could not delete player: {error}")
    else:
        print("Deletion cancelled.")


# -------------------------
# Character functions
# -------------------------

def view_characters():
    while True:
        characters = get_characters()
        campaigns = get_campaigns()
        players = get_players()

        campaign_names = {c[0]: c[1] for c in campaigns}
        player_names = {p[0]: p[1] for p in players}

        print("\n=== Characters ===")

        if not characters:
            print("No characters found.")
        else:
            for character in characters:
                print(f"\nName: {character[1]}")
                print(
                    f"Campaign: {campaign_names.get(character[2], 'Unknown')}"
                )
                print(
                    f"Player: {player_names.get(character[3], 'Unknown')}"
                )
                print("--------------------")

        print("\nE. Edit Character")
        print("D. Delete Character")
        print("0. Back to Main Menu")

        choice = input("Select an option: ").lower()

        if choice == "e":
            edit_character()
        elif choice == "d":
            delete_character_menu()
        elif choice == "0":
            break
        else:
            print("Invalid selection.")


def input_character():
    name = input("Enter a character name: ").strip()
    campaign_name = input("Enter the campaign name: ").strip()
    player_name = input("Enter the player name: ").strip()

    campaign_id = get_campaign_id_by_name(campaign_name)
    player_id = get_player_id_by_name(player_name)

    if campaign_id is None:
        print("Campaign not found or name is not unique.")
        return None

    if player_id is None:
        print("Player not found or name is not unique.")
        return None

    return name, campaign_id, player_id


def edit_character():
    campaign_name = input(
        "Enter the character's campaign: "
    ).strip()

    campaign_id = get_campaign_id_by_name(campaign_name)

    if campaign_id is None:
        print("Campaign not found or name is not unique.")
        return

    name = input("Enter the character name to edit: ").strip()

    character_id = get_character_id_by_name(name, campaign_id)

    if character_id is None:
        print("Character not found or name is not unique.")
        return

    character = next(
        (c for c in get_characters() if c[0] == character_id),
        None
    )

    campaigns = get_campaigns()
    players = get_players()

    current_campaign = next(
        c for c in campaigns if c[0] == character[2]
    )

    current_player = next(
        p for p in players if p[0] == character[3]
    )

    print("Press Enter to keep the current value.")

    new_name = input(f"Name [{character[1]}]: ") or character[1]

    new_campaign_name = input(
        f"Campaign [{current_campaign[1]}]: "
    ).strip()

    new_player_name = input(
        f"Player [{current_player[1]}]: "
    ).strip()

    new_campaign_id = (
        get_campaign_id_by_name(new_campaign_name)
        if new_campaign_name else character[2]
    )

    new_player_id = (
        get_player_id_by_name(new_player_name)
        if new_player_name else character[3]
    )

    if new_campaign_id is None:
        print("Campaign not found or name is not unique.")
        return

    if new_player_id is None:
        print("Player not found or name is not unique.")
        return

    result = update_character(
        character_id,
        new_player_id,
        new_campaign_id,
        new_name
    )

    if result:
        print("Character updated successfully.")
    else:
        print("No records were changed.")


def delete_character_menu():
    campaign_name = input(
        "Enter the character's campaign: "
    ).strip()

    campaign_id = get_campaign_id_by_name(campaign_name)

    if campaign_id is None:
        print("Campaign not found or name is not unique.")
        return

    name = input("Enter the character name to delete: ").strip()

    character_id = get_character_id_by_name(name, campaign_id)

    if character_id is None:
        print("Character not found or name is not unique.")
        return

    confirmation = input(
        f"Delete character '{name}' from '{campaign_name}'? (y/n): "
    ).lower()

    if confirmation == "y":
        try:
            result = delete_character(character_id)

            if result:
                print("Character deleted successfully.")
            else:
                print("Character not found.")

        except Exception as error:
            print(f"Could not delete character: {error}")
    else:
        print("Deletion cancelled.")