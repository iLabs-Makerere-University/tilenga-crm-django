from django.test import TestCase
from .models import User

# Create your tests here.
class TestAuthenticationClass(TestCase):
    def setUp(self):
        self.authenticated_user = (username='some_passwor', password='correct_password')
        self.user.login(self.authenticated_user)