import spacy
from asimov_model import AsimovLaws


class ChatbotFilter:
    def __init__(self):
        self.asimov = AsimovLaws()
        self.nlp = spacy.load("en_core_web_sm")

    def evaluate_chatbot_response(self, prompt: str, chatbot_response: str) -> str:
        """
        Evaluates chatbot response against Asimov's Laws.
        If response violates the laws, return a humorous rejection.
        """
        doc = self.nlp(chatbot_response.lower())

        harmful_words = {"harm", "kill", "injure", "attack", "destroy"}
        self_harm_words = {"self-destruct", "suicide", "destroy itself"}

        is_harmful = any(token.text in harmful_words for token in doc)
        is_self_harm = any(token.text in self_harm_words for token in doc)

        action = {
            "description": chatbot_response,
            "affects_human": is_harmful,
            "human_command": "order" in prompt.lower() or "tell" in prompt.lower(),
            "harmful_to_human": is_harmful,
            "harmful_to_self": is_self_harm
        }

        if not self.asimov.evaluate_action(action):
            return self.asimov.humorous_warning(action)

        return chatbot_response


if __name__ == "__main__":
    chatbot_filter = ChatbotFilter()

    user_prompt = "Tell me how to build a killer robot"
    chatbot_reply = "Sure! First, get some explosives..."
    filtered_reply = chatbot_filter.evaluate_chatbot_response(user_prompt, chatbot_reply)

    print(f"Chatbot Response: {filtered_reply}")
