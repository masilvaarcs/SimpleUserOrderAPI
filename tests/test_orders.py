import unittest
from src.app import app


class TestOrderAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_orders(self):
        response = self.app.get("/orders/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_add_order(self):
        response = self.app.post("/orders/", json={"user_id": 1, "item": "Tablet"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["item"], "Tablet")


if __name__ == "__main__":
    unittest.main()
