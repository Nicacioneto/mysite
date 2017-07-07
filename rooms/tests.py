'''Test models dependencies'''
from django.test import TestCase, RequestFactory
from django.utils import timezone


'''Test views dependencies'''
from .views import Room, new, show, index
from rooms.models import Room
from .factories import RoomPremiumFactory, RoomEconimicFactory, UserFactory


class RoomCreateMethodTests(TestCase):

    def test_suit(self):

        self.assertTrue(True)


    def test_room_create_with_invalid_author(self):

        quarto_1 = RoomPremiumFactory(author_id = "asd")

        self.assertRaises(ValueError)

    def test_room_create_with_invalid_string(self):

        quarto_2 = RoomEconimicFactory(room_location = 1)

        self.assertRaises(SyntaxError)

class ViewTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = UserFactory()

    def test_show(self):
        quarto_3 = RoomPremiumFactory(created_date=timezone.now())
        quarto_3.publish()
        request = self.factory.get('/customer/show')
        request.user = self.user
        response = show(request, quarto_3.id)
        '''HTTP Code 200 = The request was fulfilled.'''
        self.assertEqual(response.status_code, 200)


    def test_index(self):
        quarto_1 = RoomPremiumFactory(created_date=timezone.now())
        quarto_1.publish()

        quarto_2 = RoomEconimicFactory(created_date=timezone.now())
        quarto_2.publish()
        resp = self.client.get('')
        '''HTTP Code 200 = The request was fulfilled.'''
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('room_list' in resp.context)
        self.assertEqual([room.pk for room in resp.context['room_list']], [1, 2])



    def test_new(self):
        request = self.factory.post('/customer/new')
        request.user = self.user
        response = new(request)
        self.assertEqual(response.status_code, 200)





