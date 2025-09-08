from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class SignUPpPageTest(TestCase):
    username = "testuser"
    email = "testuser@test.com"
    def test_signup_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual()
        self.assertEqual(response.status_code, 200)

    def test_signup_url(self):
        response = self.client.get('signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        UserModel = get_user_model()
        user = UserModel.objects.create_user(
            self.username,
            self.email,
        )
        self.assertEqual(UserModel.objects.all().count(), 1)
        self.assertEqual(UserModel.objects.all()[0].username, user.username)
        self.assertEqual(UserModel.objects.all()[0].email, user.email)
