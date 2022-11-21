from django.test import TestCase

from .models import User


# Create your tests here.


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(email="user1@test.no")

    def test_user_creation(self):
        user = User.objects.get(email="user1@test.no")
        self.assertEqual(user.email, "user1@test.no")

    def test_user_populate_fields(self):
        user = User.objects.get(email="user1@test.no")
        user.first_name = "Test"
        user.last_name = "Testesen"
        user.save()
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "Testesen")

    def test_user_creation_with_fields(self):
        user = User.objects.create_user(
            email="user2@test.no", username="user2", password="abc123"
        )
        self.assertEqual(user.username, "user2")
        self.assertEqual(user.email, "user2@test.no")

    def test_user_creation_with_superuser(self):
        user = User.objects.create_superuser(
            email="user3@test.no", username="user3", password="def456"
        )
        self.assertEqual(user.is_superuser, True)
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.email, "user3@test.no")
