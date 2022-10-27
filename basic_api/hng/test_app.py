from rest_framework.test import APISimpleTestCase
from django.urls import reverse


class TestGetUserDetails(APISimpleTestCase):
    def test_get_user_details(self):
        url = reverse('get_user_details')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        keys = ['slackUsername', 'backend', 'age', 'bio']
        self.assertEqual(list(response.data.keys()), keys)
