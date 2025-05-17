import unittest
from weather.weather import get_weather

class TestWeather(unittest.TestCase):

    def test_get_weather_valid(self):
        city = "London"
        result = get_weather(city)
        self.assertIsNotNone(result)
        self.assertEqual(result['name'], "London")
    
    def test_get_weather_invalid(self):
        city = "InvalidCity"
        result = get_weather(city)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
