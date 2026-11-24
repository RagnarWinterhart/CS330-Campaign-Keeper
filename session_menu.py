from database import (
    create_session,
    get_campaign_id_by_name,
    get_campaigns,
    get_character_id_by_name,
    get_session_attendance_counts,
    get_sessions,
    add_attendance,
    remove_attendance,
    get_session_characters
)
# -------------------------
# Session Menu functions
# -------------------------
def remove_character_attendance(session_id, campaign_id):
    name = input("Enter character name to remove: ").strip()

    character_id = get_character_id_by_name(name, campaign_id)

    if character_id is None:
        print("Character not found or name is not unique in this campaign.")
        return

    result = remove_attendance(session_id, character_id)

    if result:
        print(f"{name} removed from attendance.")
    else:
        print(f"{name} was not assigned to this session.")


def add_character_attendance(session_id, campaign_id):
    name = input("Enter character name: ").strip()

    character_id = get_character_id_by_name(name, campaign_id)

    if character_id is None:
        print("Character not found or name is not unique in this campaign.")
        return

    try:
        add_attendance(session_id, character_id)
        print(f"{name} added to attendance.")

    except Exception as error:
        print(f"Failed to add attendance: {error}")


def manage_attendance():
    sessions = get_sessions()

    if not sessions:
        print("No sessions found.")
        return

    session_id = input("Enter session ID: ")

    if not session_id.isdigit():
        print("Invalid session ID.")
        return

    session_id = int(session_id)

    selected_session = next(
        (session for session in sessions if session[0] == session_id),
        None
    )

    if selected_session is None:
        print("Session not found.")
        return

    campaign_id = selected_session[1]

    while True:
        characters = get_session_characters(session_id)

        print(f"\n=== Attendance: {selected_session[2]} ===")

        if not characters:
            print("No characters assigned yet.")
        else:
            for character in characters:
                print(character[1])

        print("\nA. Add Character")
        print("R. Remove Character")
        print("0. Back")

        choice = input("Select an option: ").lower()

        if choice == "a":
            add_character_attendance(session_id, campaign_id)

        elif choice == "r":
            remove_character_attendance(session_id, campaign_id)

        elif choice == "0":
            break

        else:
            print("Invalid selection.")


def view_sessions():
    while True:
        sessions = get_sessions()
        campaigns = get_campaigns()

        campaign_names = {c[0]: c[1] for c in campaigns}

        print("\n=== Game Sessions ===")

        if not sessions:
            print("No sessions found.")
        else:
            for session in sessions:
                print(f"\nID: {session[0]}")
                print(
                    f"Campaign: {campaign_names.get(session[1], 'Unknown')}"
                )
                print(f"Name: {session[2]}")
                print(f"Date: {session[3]}")
                print(f"Notes: {session[4]}")
                print("--------------------")

        print("\nA. Manage Attendance")
        print("0. Back to Main Menu")

        choice = input("Select an option: ").lower()

        if choice == "a":
            manage_attendance()
        elif choice == "0":
            break
        else:
            print("Invalid selection.")
            
            
def create_session_menu():
    campaigns = get_campaigns()

    if not campaigns:
        print("You need to create a campaign first.")
        return

    print("\n=== Available Campaigns ===")

    for campaign in campaigns:
        print(campaign[1])

    campaign_name = input(
        "\nEnter the campaign name: "
    ).strip()

    campaign_id = get_campaign_id_by_name(campaign_name)

    if campaign_id is None:
        print("Campaign not found or name is not unique.")
        return

    session_name = input("Enter session name: ").strip()
    session_date = input("Enter session date (YYYY-MM-DD): ").strip()
    notes = input("Enter session notes: ").strip()

    try:
        session_id = create_session(
            campaign_id,
            session_name,
            session_date,
            notes
        )

        print(f"Session created successfully! ID: {session_id}")

    except Exception as error:
        print(f"Failed to create session: {error}")
        
def session_attendance_report():
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