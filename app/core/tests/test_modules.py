from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTestCases(TestCase):

    def test_create_user_with_successful(self):
        """Test Case for create user with email is successful"""
        email = 'example@gmail.com'
        password = 'Test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email),
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normaloized(self):
        """Test the email for a new user is normalized"""
        email = 'example@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_with_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_super_user(self):
        """Test case for create the super user"""
        user = get_user_model().objects.create_superuser(
            'example@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
