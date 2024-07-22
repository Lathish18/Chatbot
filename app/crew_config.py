class SimpleBot:
    def __init__(self):
        self.intents = {
            "greeting": self.greet_intent,
            "how_are_you": self.how_are_you_intent,
            "news": self.news_intent,
            "time": self.time_intent,
            "joke": self.joke_intent,
            "quote": self.quote_intent,
            "define": self.define_intent,
            "reminder": self.reminder_intent,
            "recipe": self.recipe_intent,
            "sports": self.sports_intent,
            "music": self.music_intent
        }

    def handle_message(self, intent, message, sender_name):
        handler = self.intents.get(intent, self.default_intent)
        return handler(message, sender_name)

    def greet_intent(self, message, sender_name):
        return f"Hey {sender_name}, how can I assist you today?"

    def how_are_you_intent(self, message, sender_name):
        return "I'm doing well, thanks! How about you? How can I help today?"

    def news_intent(self, message, sender_name):
        return "I can provide the latest news. What topic are you interested in?"

    def time_intent(self, message, sender_name):
        return "I can tell you the current time. Where are you located?"

    def joke_intent(self, message, sender_name):
        return "I can tell you a joke. Want to hear one?"

    def quote_intent(self, message, sender_name):
        return "I can share an inspiring quote with you. Would you like one?"

    def define_intent(self, message, sender_name):
        return "I can define words for you. What word would you like defined?"

    def reminder_intent(self, message, sender_name):
        return "I can set reminders for you. What would you like to be reminded about?"

    def recipe_intent(self, message, sender_name):
        return "I can provide recipes. What kind of dish are you looking for?"

    def sports_intent(self, message, sender_name):
        return "I can provide sports updates. Which sport are you interested in?"

    def music_intent(self, message, sender_name):
        return "I can recommend music. What genre or artist do you like?"

    def default_intent(self, message, sender_name):
        return "Sorry, I don't understand that."

# Example usage
bot = SimpleBot()
response = bot.handle_message("greeting", "Hello!", "Lathish")
print(response)
