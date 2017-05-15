from django.test import TestCase
from wheel.signatures import assertTrue

from .models import Room
from django.utils import timezone


class RoomCreateMethodTests(TestCase):

    def test_suit(self):
        self.assertTrue(True)


    def test_room_create(self):

        quarto_1 = Room(
        room_title="Suíte Presidencial",
        room_location = "Decimo andar, cobertura",
        room_description = "Suite super luxo, com cama kingsize, frigobar, ar condicionado",
        created_date=timezone.now(),
        pub_date=timezone.now(),
        author_id = "asd"
        )
        self.assertRaises(ValueError)

        quarto_2 = Room(
        room_title=1,
        room_location = 2,
        room_description = 3,
        created_date=timezone.now(),
        pub_date=timezone.now(),
        author_id = "1")

        self.assertRaises(SyntaxError)
