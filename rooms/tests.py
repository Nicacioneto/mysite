from django.test import TestCase, RequestFactory
from .models import Room
from django.utils import timezone


from django.contrib.auth.models import AnonymousUser, User
from .views import Room, new, show, index



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

class ViewTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='nicacio', email='nicacionetobsb@gmail.com', password='admin')

    def test_show(self):
        quarto_3 = Room(
            room_title="Suíte Presidencial",
            room_location="Decimo andar, cobertura",
            room_description="Suite super luxo, com cama kingsize, frigobar, ar condicionado",
            created_date=timezone.now(),
            pub_date=timezone.now(),
            author_id="1")
        quarto_3.save()
        request = self.factory.get('/customer/show')
        request.user = self.user
        response = show(request, quarto_3.id)
        self.assertEqual(response.status_code, 200)