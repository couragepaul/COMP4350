from django.test import TestCase
from django.contrib.auth.models import User

class UserTestCase(TestCase):

    def test_user_create(self):
        name = 'Timmy the Tester'
        user = User.objects.create_user(name, 'blahblah@gmail.com', 'password')
        self.assertTrue(User.objects.get(username=name))

    def test_user_delete(self):
        name = 'Timmy the Tester'
        user = User.objects.create_user(name, 'blahblah@gmail.com', 'password')
        User.objects.get(username=name)
        self.assertTrue(User.objects.get(username=name).delete())

    def test_get_user(self):
        name = 'Timmy the Tester'
        user = User.objects.create_user(name, 'blahblah@gmail.com', 'password')
        User.objects.get(username=name)
        self.assertTrue(User.objects.get(username=name))
