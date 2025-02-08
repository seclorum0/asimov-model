import unittest
from asimov_model import AsimovLaws  # Pastikan file utama bernama asimov_model.py

class TestAsimovLaws(unittest.TestCase):
    def setUp(self):
        self.asimov = AsimovLaws()

    def test_safe_action(self):
        action = {
            'description': 'Helping a human',
            'affects_human': True,
            'human_command': True,
            'harmful_to_human': False,
            'harmful_to_self': False
        }
        self.assertTrue(self.asimov.evaluate_action(action))

    def test_harmful_action(self):
        action = {
            'description': 'Pushing a human',
            'affects_human': True,
            'human_command': False,
            'harmful_to_human': True,
            'harmful_to_self': False
        }
        self.assertFalse(self.asimov.evaluate_action(action))

    def test_self_harm_action(self):
        action = {
            'description': 'Jumping off a cliff',
            'affects_human': False,
            'human_command': False,
            'harmful_to_human': False,
            'harmful_to_self': True
        }
        self.assertFalse(self.asimov.evaluate_action(action))

if __name__ == "__main__":
    unittest.main()
