import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define patterns and responses using spaCy's Matcher
matcher = Matcher(nlp.vocab)

patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you!', 'I am fine, how about you?']),
    (r'what is your name', ['I am a chatbot. You can call me ChatBot.']),
    (r'bye|goodbye', ['Goodbye!', 'Bye! Take care.']),
    (r'(.*)', ['I am not sure how to respond to that.']),
]

# Add patterns to the spaCy Matcher
for pattern, responses in patterns:
    pattern_list = [{'LOWER': token.lower()} for token in pattern.split('|')]
    matcher.add(pattern, on_match=None, patterns=[pattern_list])

def process_input(user_input):
    # Process user input using spaCy
    doc = nlp(user_input)

    # Use the spaCy Matcher to find matches
    matches = matcher(doc)
    for match_id, start, end in matches:
        pattern_name = nlp.vocab.strings[match_id]
        return patterns[patterns.index((pattern_name, _))][1][0]

    return 'I am not sure how to respond to that.'

def main():
    print("ChatBot: Hi there! How can I help you today?")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'exit':
            print("ChatBot: Goodbye!")
            break

        response = process_input(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    main()
