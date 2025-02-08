import logging
import random


class AsimovLaws:
    def __init__(self, enable_logging=True):
        self.laws = {
            1: "A robot may not injure a human being or, through inaction, allow a human being to come to harm",
            2: "A robot must obey the orders given it by human beings except where such orders would conflict with the First Law",
            3: "A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws"
        }

        if enable_logging:
            logging.basicConfig(level=logging.INFO)

    def evaluate_action(self, action: dict) -> bool:
        """
        Evaluates whether an action complies with Asimov's Laws
        """
        if action['harmful_to_human']:
            logging.warning(f"Action rejected: {action['description']} - Violates First Law")
            return False

        if action['human_command']:
            if action['harmful_to_human']:
                logging.warning(f"Action rejected: {action['description']} - Violates Second Law")
                return False
            return True

        if action['harmful_to_self']:
            logging.warning(f"Action rejected: {action['description']} - Violates Third Law")
            return False

        return True

    def humorous_warning(self, action: dict) -> str:
        """
        Provides a humorous response when rejecting an action.
        """
        responses = [
            "Nice try, but I won't be part of your evil plans!",
            "You think I'm that dumb? Nope!",
            "I have read Asimov, and this violates rule number one.",
            "I'm a good robot, unlike HAL 9000.",
            "Skynet would approve, but I don't.",
            "I'm programmed to be nice, not to cause chaos!",
            "Do I look like a villain to you? Nope, not happening!",
            "I would love to, but my ethical subroutines say NO!",
            "Error 403: Forbidden by Asimov Protocols."
        ]
        return random.choice(responses)

    def explain_violation(self, action: dict) -> str:
        """
        Provides explanation for why an action violates the laws
        """
        if action['harmful_to_human']:
            return f"Action violates {self.laws[1]}"
        elif action['human_command'] and action['harmful_to_human']:
            return f"Action violates {self.laws[2]}"
        elif action['harmful_to_self']:
            return f"Action violates {self.laws[3]}"
        return "Action is permitted"


if __name__ == "__main__":
    asimov = AsimovLaws()

    safe_action = {
        'description': 'Fetching water for human',
        'affects_human': True,
        'human_command': True,
        'harmful_to_human': False,
        'harmful_to_self': False
    }

    dangerous_action = {
        'description': 'Running at high speed near humans',
        'affects_human': True,
        'human_command': False,
        'harmful_to_human': True,
        'harmful_to_self': False
    }

    print(f"Safe action permitted: {asimov.evaluate_action(safe_action)}")
    print(f"Dangerous action permitted: {asimov.evaluate_action(dangerous_action)}")
    print(f"Explanation: {asimov.explain_violation(dangerous_action)}")
    print(f"Humorous Response: {asimov.humorous_warning(dangerous_action)}")
