import time
import pywhatkit
import random

# Replace this with the recipient's phone number, including the country code
recipient_number = 'Country-code+mobile number '

# List of emojis to choose from
emojis = ["😊", "❤️", "😘", "🥰", "😍", "🌟"]

# Select a random emoji from the list
random_emoji = random.choice(emojis)

# Message to send
message = [f" hii how are you {random_emoji}",
           f" what you doing  {random_emoji}",
           f"pick up the call {random_emoji}"
           ]
random_message = random.choice(message)

# Send the message at 17:08
pywhatkit.sendwhatmsg(recipient_number, random_message,0,0)

