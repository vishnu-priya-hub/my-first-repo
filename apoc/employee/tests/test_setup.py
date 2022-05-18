
from django.urls import reverse
from rest_framework.test import APITestCase


class TestSetUp(APITestCase):

    def SetUp(self):
        self.api_url = reverse('api')
        self.login_url = reverse('login')

        self.user_data = {
        'name': "Navitha",
        'location': "hyderabad",
        'industry': "cg",
        'phone_number': "9012345678",
        'email_id': "email@gmail.com"
    }
        return super().setUp()

    @property
    def tearDown(self):
        return super().tearDown