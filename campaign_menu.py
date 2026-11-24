# -------------------------
# Campaign functions
# -------------------------

from database import delete_campaign, get_campaign_id_by_name, get_campaigns, update_campaign


def view_campaigns():
    while True:
        campaigns = get_campaigns()

        print("\n=== Campaigns ===")

        if not campaigns:
            print("No campaigns found.")
        else:
            for campaign in campaigns:
                print(f"\nName: {campaign[1]}")
                print(f"System: {campaign[2]}")
                print(f"Description: {campaign[3]}")
                print("--------------------")

        print("\nE. Edit Campaign")
        print("D. Delete Campaign")
        print("0. Back to Main Menu")

        choice = input("Select an option: ").lower()

        if choice == "e":
            edit_campaign()
        elif choice == "d":
            delete_campaign_menu()
        elif choice == "0":
            break
        else:
            print("Invalid selection.")


def input_campaign():
    name = input("Enter a campaign name: ").strip()
    game_system = input("Enter the game system: ").strip()
    description = input("Enter a short description: ").strip()

    return name, game_system, description


def edit_campaign():
    name = input("Enter the campaign name to edit: ").strip()
    campaign_id = get_campaign_id_by_name(name)

    if campaign_id is None:
        print("Campaign not found or name is not unique.")
        return

    campaign = next(
        (c for c in get_campaigns() if c[0] == campaign_id),
        None
    )

    print("Press Enter to keep the current value.")

    new_name = input(f"Name [{campaign[1]}]: ") or campaign[1]
    game_system = input(f"System [{campaign[2]}]: ") or campaign[2]
    description = input(f"Description [{campaign[3]}]: ") or campaign[3]

    result = update_campaign(
        campaign_id, new_name, game_system, description
    )

    if result:
        print("Campaign updated successfully.")
    else:
        print("No records were changed.")


def delete_campaign_menu():
    name = input("Enter the campaign name to delete: ").strip()
    campaign_id = get_campaign_id_by_name(name)

    if campaign_id is None:
        print("Campaign not found or name is not unique.")
        return

    confirmation = input(
        f"Delete campaign '{name}'? (y/n): "
    ).lower()

    if confirmation == "y":
        try:
            result = delete_campaign(campaign_id)

            if result:
                print("Campaign deleted successfully.")
            else:
                print("Campaign not found.")

        except Exception as error:
            print(f"Could not delete campaign: {error}")
    else:
        print("Deletion cancelled.")
