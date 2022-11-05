from rest_framework.test import APISimpleTestCase
from django.urls import reverse
import pytest


class TestGetUserDetails(APISimpleTestCase):
    def test_get_user_details(self):
        url = reverse('get_user_details')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        keys = ['slackUsername', 'backend', 'age', 'bio']
        self.assertEqual(list(response.data.keys()), keys)


@pytest.mark.parametrize(
    'operation_type, x, y, result',
    [
        ('addition', 1, 2, 3),
        ('subtraction', 1, 2, -1),
        ('multiplication', 1, 2, 2),
        ('addition', 4, 2, 6),
        ('subtraction', 4, 2, 2),
        ('multiplication', 4, 2, 8),
        ('addition', 10, 2, 12),
        ('subtraction', 10, 2, 8),
        ('multiplication', 10, 2, 20),
    ]
)
def test_calculate(operation_type, x, y, result, client):
    data = {
        "operation_type": operation_type,
        "x": x,
        "y": y
    }

    url = reverse('calculate')
    response = client.post(url, data, format='json')
    assert response.status_code == 200
    assert response.data['result'] == result
