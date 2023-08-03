import unittest
from src.person import Person
from src.song import Song
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Dancing Queen", 10)
        self.person_1 = Person("Aiden", 10.00, "Abba")
        self.song_1 = Song("Dave", "Psycho")
        self.song_2 = Song("Rick Astley", "Never Gonna Give You Up")
        self.song_3 = Song("Justin Bieber", "Baby")
        self.playlist_1 = [self.song_1, self.song_2, self.song_3] 

    def test_capacity_in_the_room(self):
        self.assertEqual(10, self.room_1.max_capacity)

    def test_add_person_to_room(self):
        self.room_1.add_person(self.person_1)
        self.assertEqual("Aiden", self.room_1.room[0].name)

    def test_add_a_person_then_remove_person_from_the_room(self):
        self.room_1.add_person(self.person_1)
        self.assertEqual("Aiden", self.room_1.room[0].name)
        self.room_1.remove_person(self.person_1)
        self.assertEqual([], self.room_1.room)

    def test_add_song_to_room(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual("Psycho", self.room_1.room[0].title)

    def test_current_capacity_after_adding_a_person(self):
        self.room_1.add_person(self.person_1)
        self.assertEqual(10, self.room_1.max_capacity)

    def test_max_capacity(self):
        room_2 = Room("Dancing Queen", 0)
        self.room_1.add_person(self.person_1)
        self.assertEqual(0, len(room_2.room))

    def test_check_customers_wallet(self):
        self.person_1.charge_customer(5.00)
        self.assertEqual(5.00, self.person_1.wallet)

    def test_add_fee_to_till(self):
        self.room_1.add_till(5.00)
        self.assertEqual(5.00, self.room_1.till)

    def test_charge_customer_wallet_and_add_to_till(self):
        self.person_1.charge_customer(5.00)
        self.assertEqual(5.00, self.person_1.wallet)
        self.room_1.add_till(5.00)
        self.assertEqual(5.00, self.room_1.till)

    def test_charge_customer(self):
        self.room_1.charge_customer(self.person_1, 5.00)
        self.assertEqual(5.00, self.person_1.wallet)
        self.assertEqual(5.00, self.room_1.till)

    def test_favourite_song_is_in_the_room(self):
        self.room_1.add_playlist(self.song_1)
        self.assertEqual("Baby", self.playlist_1[2].title)

    def test_add_playlist_and_check_favourite_song(self):
        self.room_1.add_playlist(self.song_1)

        result = self.room_1.favourite_song("Psycho")
        self.assertEqual("Woooo!", result)

        

