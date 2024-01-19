# Simple Chatbot using spaCy

This simple chatbot is implemented in Python using the spaCy library. It recognizes certain patterns in user input and provides predefined responses.

## Usage

1. Install Dependencies:
   - Make sure you have Python installed on your system.
   - Create and activate a virtual environment (optional but recommended):

     ```bash
     python -m venv venv  # Create a virtual environment
     source venv/bin/activate  # Activate on Linux/Mac
     .\venv\Scripts\activate  # Activate on Windows
     ```

   - Install spaCy using the following command:

     ```bash
     pip install spacy
     ```

   - Download the English language model for spaCy:

     ```bash
     python -m spacy download en_core_web_sm
     ```

2. Run the Chatbot:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the `chatbot.py` file.
   - Run the chatbot script:

     ```bash
     python chatbot.py
     ```

3. Interact with the Chatbot:
   - Enter your messages when prompted.
   - Type 'exit' to end the conversation.

## Dependencies

- Python 3.x
- spaCy library
- English language model for spaCy (`en_core_web_sm`)

## Notes

- The chatbot recognizes certain patterns using spaCy's Matcher.
- Feel free to customize the patterns and responses to make the chatbot more interactive.

