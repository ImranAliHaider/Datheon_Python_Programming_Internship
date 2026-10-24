"""Simple rule-based customer support bot. Run: python chatbot.py"""
import re

FAQ = {
    "hours": {
        "patterns": [r"\b(hours|open|opening|close|closing|time)\b"],
        "answer": "Our sample business hours are Monday-Friday, 9:00 AM to 5:00 PM."
    },
    "shipping": {
        "patterns": [r"\b(ship|shipping|delivery|deliver|tracking)\b"],
        "answer": "Standard delivery usually takes 3-5 business days. This is sample FAQ information."
    },
    "returns": {
        "patterns": [r"\b(return|refund|exchange|replace)\b"],
        "answer": "Sample policy: contact support within 14 days of receiving your order to ask about a return."
    },
    "price": {
        "patterns": [r"\b(price|cost|pricing|fee|charge)\b"],
        "answer": "Please tell me which product you mean, or check the product listing for its current price."
    },
    "contact": {
        "patterns": [r"\b(contact|email|phone|support|human|agent)\b"],
        "answer": "You can reach our sample support team at support@example.com."
    },
    "thanks": {
        "patterns": [r"\b(thanks|thank you|thx)\b"],
        "answer": "You're welcome! Is there anything else I can help with?"
    },
}

GREETINGS = {"hi", "hello", "hey", "good morning", "good afternoon", "good evening"}
EXIT_WORDS = {"bye", "exit", "quit"}

def get_response(message):
    text = message.lower().strip()
    if not text:
        return "Please type a question so I can help."
    if text in EXIT_WORDS or re.search(r"\b(bye|exit|quit)\b", text):
        return "Goodbye! Thanks for chatting."
    if text in GREETINGS or re.match(r"^(hi|hello|hey)\b", text):
        return "Hello! Ask me about business hours, shipping, returns, prices, or support."
    matches = []
    for intent, details in FAQ.items():
        if any(re.search(pattern, text) for pattern in details["patterns"]):
            matches.append(details["answer"])
    if matches:
        # Multiple matched intents are returned together rather than ignoring part of the question.
        return "\n".join(dict.fromkeys(matches))
    return "Sorry, I didn't understand. Try asking about hours, shipping, returns, prices, or support."

def main():
    print("=== CUSTOMER SUPPORT BOT ===")
    print("Ask about hours, shipping, returns, prices, or support. Type 'bye' to exit.")
    while True:
        try:
            message = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye!")
            break
        response = get_response(message)
        print("Bot:", response)
        if message.strip().lower() in EXIT_WORDS or re.search(r"\b(bye|exit|quit)\b", message.lower()):
            break

if __name__ == "__main__":
    main()
