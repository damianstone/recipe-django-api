
from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    # test creting a new user with a email successful
    def test_create_user_email(self):
        email = 'damianstone@gmail.com'
        password = 'testpass1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        # check email = email
        self.assertEqual(user.email, email)
        # true is the password is correct
        self.assertTrue(user.check_password(password))

    # email normalize
    # error if the email is is uppercase
    def test_new_user_lowercase(self):
        email = 'damianstone@gmail.COM'
        user = get_user_model().objects.create_user(email, 'password123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')
    
    def test_superuser(self):
        user = get_user_model().objects.create_superuser(
            'damianstonedev@gmail.com',
            'test1234'
        )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
