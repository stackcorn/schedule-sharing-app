from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class RoomTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='room_name', password='password')

    def test_saved_room(self):
        self.assertEqual(User.objects.count(), 1)