import sys, unittest, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from model.categorizer import predict
from model.forecaster import forecast_next_month
from llm import chat
from app import db

class TestCategorizer(unittest.TestCase):
    def test_food(self):       self.assertEqual(predict("Zomato dinner order"), "Food")
    def test_transport(self):  self.assertEqual(predict("Uber ride to office"), "Transport")
    def test_bills(self):      self.assertEqual(predict("Electricity bill"), "Bills")
    def test_health(self):     self.assertEqual(predict("Apollo pharmacy medicines"), "Health")
    def test_entertainment(self): self.assertEqual(predict("Netflix subscription"), "Entertainment")

class TestForecaster(unittest.TestCase):
    def test_empty(self):      self.assertEqual(forecast_next_month([]), 0.0)
    def test_single(self):     self.assertEqual(forecast_next_month([500]), 500.0)
    def test_trend(self):      self.assertAlmostEqual(forecast_next_month([100, 200, 300]), 400.0, places=3)
    def test_non_negative(self): self.assertGreaterEqual(forecast_next_month([300, 200, 100]), 0.0)

class TestDatabase(unittest.TestCase):
    def test_add_and_read(self):
        db.DB = Path(tempfile.mkdtemp()) / "t.db"
        db.add_expense("2026-09-01", "Tea", 20, "Food")
        df = db.get_expenses()
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]["category"], "Food")

class TestChat(unittest.TestCase):
    def test_no_key(self):
        import os
        for k in ("LLM_API_KEY", "LLM_API_URL"): os.environ.pop(k, None)
        chat.load_dotenv = lambda *a, **k: None
        self.assertIn("not configured", chat.ask("x", "y"))

if __name__ == "__main__":
    unittest.main(verbosity=2)
