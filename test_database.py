# DO NOT RUN IF YOU HAVE REAL DATA IN THE DATABASE
import unittest

from database import (
    create_campaign,
    create_player,
    create_character,
    get_characters,
    update_character, 
    get_connection
)


class TestCharacterUpdates(unittest.TestCase):

    def setUp(self):
        """Create fresh test records before each test."""
        self.campaign1_id = create_campaign(
            "Test Campaign One", "D&D 5e", "First test campaign"
        )

        self.campaign2_id = create_campaign(
            "Test Campaign Two", "Pathfinder 2e", "Second test campaign"
        )

        self.player1_id = create_player("Test Player One")
        self.player2_id = create_player("Test Player Two")

        self.character_id = create_character(
            "Test Character",
            self.campaign1_id,
            self.player1_id
        )
        
    def tearDown(self):
        connection = None
        cursor = None

        try:
            connection = get_connection()
            cursor = connection.cursor()

            # Delete dependent records first
            cursor.execute("DELETE FROM player_character")
            cursor.execute("DELETE FROM player")
            cursor.execute("DELETE FROM campaign")

            # Reset auto-increment counters
            cursor.execute("ALTER TABLE player_character AUTO_INCREMENT = 1")
            cursor.execute("ALTER TABLE player AUTO_INCREMENT = 1")
            cursor.execute("ALTER TABLE campaign AUTO_INCREMENT = 1")

            connection.commit()

        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None and connection.is_connected():
                connection.close()

    def get_test_character(self):
        """Retrieve the character created for this test."""
        characters = get_characters()

        for character in characters:
            if character[0] == self.character_id:
                return character

        return None

    def test_update_character_name(self):
        update_character(
            self.character_id,
            self.player1_id,
            self.campaign1_id,
            "Updated Character"
        )

        character = self.get_test_character()

        self.assertEqual(character[3], "Updated Character")

    def test_update_character_player(self):
        update_character(
            self.character_id,
            self.player2_id,
            self.campaign1_id,
            "Test Character"
        )

        character = self.get_test_character()

        self.assertEqual(character[2], self.player2_id)

    def test_update_character_campaign(self):
        update_character(
            self.character_id,
            self.player1_id,
            self.campaign2_id,
            "Test Character"
        )

        character = self.get_test_character()

        self.assertEqual(character[1], self.campaign2_id)

    def test_update_all_character_fields(self):
        update_character(
            self.character_id,
            self.player2_id,
            self.campaign2_id,
            "Fully Updated Character"
        )

        character = self.get_test_character()

        self.assertEqual(character[1], self.campaign2_id)
        self.assertEqual(character[2], self.player2_id)
        self.assertEqual(character[3], "Fully Updated Character")

    def test_invalid_player_id(self):
        original_character = self.get_test_character()

        with self.assertRaises(Exception):
            update_character(
                self.character_id,
                999999,
                self.campaign1_id,
                "Invalid Update"
            )

        character = self.get_test_character()

        self.assertEqual(character, original_character)


if __name__ == "__main__":
    unittest.main()
