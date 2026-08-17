import unittest

from seccion1 import summarize_by_movie, validate_showtime


class TestSeccion1(unittest.TestCase):

    def test_summarize_by_movie(self):
        showtimes = [
            {"movie": "Inside Out 3", "cine": "Perisur", "format": "IMAX", "tickets_sold": 120},
            {"movie": "Inside Out 3", "cine": "Perisur", "format": "2D", "tickets_sold": 85},
            {"movie": "Inside Out 3", "cine": "Santa Fe", "format": "2D", "tickets_sold": 90},
            {"movie": "Deadpool 4", "cine": "Perisur", "format": "3D", "tickets_sold": 200},
            {"movie": "Deadpool 4", "cine": "Santa Fe", "format": "IMAX", "tickets_sold": 180},
            {"movie": "Moana 3", "cine": "Perisur", "format": "2D", "tickets_sold": 60},
        ]

        result = summarize_by_movie(showtimes)

        self.assertEqual(result[0]["movie"], "Deadpool 4")
        self.assertEqual(result[0]["total_shows"], 2)
        self.assertEqual(result[0]["total_tickets"], 380)
        self.assertEqual(result[0]["avg_tickets"], 190.0)

    def test_valid_showtime(self):
        result = validate_showtime("14:30", 120, "10:00", "23:00")

        self.assertEqual(result, {"valid": True})

    def test_showtime_before_opening(self):
        result = validate_showtime("09:00", 90, "10:00", "23:00")

        self.assertFalse(result["valid"])
        self.assertIn("Starts before opening", result["reason"])

    def test_showtime_after_closing(self):
        result = validate_showtime("21:30", 150, "10:00", "23:00")

        self.assertFalse(result["valid"])
        self.assertIn("Ends after closing", result["reason"])

    def test_showtime_ending_at_closing(self):
        result = validate_showtime("21:00", 120, "10:00", "23:00")

        self.assertFalse(result["valid"])


if __name__ == "__main__":
    unittest.main()