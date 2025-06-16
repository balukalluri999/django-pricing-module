from rest_framework.test import APITestCase
from pricing.models import PricingConfig

class PricingConfigAPITestCase(APITestCase):

    def setUp(self):
        self.url = "/api/configs/"  # Direct URL path instead of reverse()
        self.valid_payload = {
            "base_fare": 50,
            "price_per_km": 10,
            "price_per_minute": 2,
            "active_days": ["Monday", "Tuesday"],
            "start_time": "08:00:00",
            "end_time": "20:00:00"
        }
        self.config = PricingConfig.objects.create(**self.valid_payload)

    def test_get_all_configs(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["base_fare"], "50.00")

    def test_create_config(self):
        new_payload = {
            "base_fare": 60,
            "price_per_km": 12,
            "price_per_minute": 3,
            "active_days": ["Wednesday"],
            "start_time": "09:00:00",
            "end_time": "18:00:00"
        }
        response = self.client.post(self.url, new_payload, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(PricingConfig.objects.count(), 2)
        self.assertEqual(response.data["base_fare"], "60.00")

    def test_invalid_config_post(self):
        invalid_payload = {
            "base_fare": "invalid",  # should be number
            "price_per_km": 10,
            "price_per_minute": 2,
            "active_days": ["Thursday"],
            "start_time": "08:00:00",
            "end_time": "20:00:00"
        }
        response = self.client.post(self.url, invalid_payload, format='json')
        self.assertEqual(response.status_code, 400)
