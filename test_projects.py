"""Basic automated tests. Run: python -m unittest -v"""
import tempfile
import unittest
from pathlib import Path

from portfolio import summarize
from organizer import organize_folder
from chatbot import get_response

class ProjectTests(unittest.TestCase):
    def test_portfolio_profit(self):
        rows = summarize([{
            "ticker": "ABC", "buy_price": 10.0, "quantity": 5, "current_price": 12.0
        }])
        self.assertAlmostEqual(rows[0]["invested"], 50)
        self.assertAlmostEqual(rows[0]["market_value"], 60)
        self.assertAlmostEqual(rows[0]["gain_loss"], 10)
        self.assertAlmostEqual(rows[0]["gain_loss_percent"], 20)

    def test_chatbot_hours(self):
        self.assertIn("business hours", get_response("When do you close?"))

    def test_chatbot_multiple_intents(self):
        response = get_response("What are your shipping and return policies?")
        self.assertIn("delivery", response.lower())
        self.assertIn("return", response.lower())

    def test_chatbot_exit(self):
        self.assertIn("Goodbye", get_response("bye"))

    def test_organizer_preview_then_move(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "notes.txt").write_text("hello", encoding="utf-8")
            moved, skipped, errors = organize_folder(root, dry_run=True)
            self.assertEqual(len(moved), 1)
            self.assertTrue((root / "notes.txt").exists())
            moved, skipped, errors = organize_folder(root, dry_run=False)
            self.assertEqual(len(moved), 1)
            self.assertTrue((root / "Documents" / "notes.txt").exists())
            self.assertEqual(errors, [])

if __name__ == "__main__":
    unittest.main()
