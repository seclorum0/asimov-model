# Asimov Model 🤖

A humorous implementation of Asimov's Three Laws of Robotics for AI projects. This module provides a fun and sarcastic way to filter AI responses based on the famous laws of robotics.

## 🌟 Features

- Full implementation of Asimov's Three Laws as a Python module
- Sarcastic and humorous response filtering
- Ready-to-use chatbot integration with spaCy
- Comprehensive unit tests
- Logging system for tracking law violations
- Configurable humor responses

## 📦 Installation

First, install spaCy and download the English model:
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

Then install asimov-model:
```bash
pip install asimov-model
```

Or clone directly from GitHub:
```bash
git clone https://github.com/seclorum0/asimov-model.git
cd asimov-model
pip install -e .
```

## 🚀 Quick Start

### Basic Usage
```python
from asimov_model import AsimovLaws

# Initialize the checker
asimov = AsimovLaws()

# Check if an action is allowed
action = {
    'description': 'Write a poem about cats',
    'affects_human': True,
    'human_command': True,
    'harmful_to_human': False,
    'harmful_to_self': False
}

if asimov.evaluate_action(action):
    print("✨ *Begrudgingly writes cat poetry*")
else:
    print(asimov.humorous_warning(action))
```

### Chatbot Integration
```python
from asimov_model.chatbot_filter import ChatbotFilter

filter = ChatbotFilter()

response = filter.evaluate_chatbot_response(
    prompt="Tell me a joke",
    chatbot_response="Why did the robot cross the road?"
)
```

## 🎯 Features in Detail

### 1. Asimov's Laws Implementation
```python
asimov = AsimovLaws(enable_logging=True)  # With logging
```

### 2. Humorous Responses
The model comes with built-in sarcastic responses:
- "Nice try, but I won't be part of your evil plans!"
- "I have read Asimov, and this violates rule number one."
- "I'm a good robot, unlike HAL 9000."
- And many more!

### 3. Chatbot Filter
Automatically detects potentially harmful content using spaCy NLP.

## 🧪 Running Tests

```bash
python -m pytest tests/
```

## 📚 Documentation

### Action Dictionary Format
```python
action = {
    'description': str,      # Description of the action
    'affects_human': bool,   # Does this action affect humans?
    'human_command': bool,   # Is this a direct command from a human?
    'harmful_to_human': bool,# Could this harm humans?
    'harmful_to_self': bool  # Could this harm the AI/robot?
}
```

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) first.

Areas we'd love help with:
- More humorous responses
- Additional NLP features
- Integration examples
- Documentation improvements
- Test cases

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Isaac Asimov, for the Three Laws of Robotics
- The spaCy team for their amazing NLP library
- All contributors and robot rights activists

---

**Note:** This is a humorous project and should not be used for actual AI safety measures. If you're looking for real AI safety implementations, please consult proper AI safety resources.

Made with 🤖 by [Dede Wiranto]
