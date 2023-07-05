import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestAPI(unittest.TestCase):
    def test_get_health(self):
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "OK", "message": "Server is running"})

    def test_suggest_cities(self):
        query = "London"
        latitude = 51.5074
        longitude = -0.1278

        response = client.get(f"/api/suggestions?q={query}&latitude={latitude}&longitude={longitude}")
        self.assertEqual(response.status_code, 200)
        suggestions = response.json().get("suggestions")
        self.assertIsInstance(suggestions, list)
        self.assertLessEqual(len(suggestions), 10)
        for suggestion in suggestions:
            self.assertIsInstance(suggestion, dict)
            self.assertIn("name", suggestion)
            self.assertIn("latitude", suggestion)
            self.assertIn("longitude", suggestion)
            self.assertIn("score", suggestion)

if __name__ == "__main__":
    unittest.main()
