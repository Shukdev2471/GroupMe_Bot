import requests
import time
import os  # Add this at the top

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")  # Replace your hardcoded token
GROUP_ID = os.environ.get("GROUP_ID")         # Replace your hardcoded group ID
BOT_ID = os.environ.get("BOT_ID")  

# API URLs
MESSAGES_API_URL = f"https://api.groupme.com/v3/groups/{GROUP_ID}/messages?token={ACCESS_TOKEN}"
SEND_MESSAGE_URL = "https://api.groupme.com/v3/bots/post"

# Person to track
# TARGET_USER = "Aayush Chaudhary"
TARGET_USER = "Noorus Sabiha Shaik"

def get_latest_message():
    """Fetch the latest message from the GroupMe group."""
    response = requests.get(MESSAGES_API_URL)
    if response.status_code == 200:
        messages = response.json()["response"]["messages"]
        if messages:
            return messages[0]  # Latest message
    return None

def send_message(text):
    """Send a message to the GroupMe chat."""
    data = {
        "bot_id": BOT_ID,
        "text": text
    }
    requests.post(SEND_MESSAGE_URL, json=data)
    print(f"✅ Sent: {text}")

def auto_reply():
    """Continuously listen for new messages and reply if needed."""
    last_message_id = None

    while True:
        message = get_latest_message()
        if message and message["id"] != last_message_id:
            sender = message["name"]
            text = message["text"]

            if sender == TARGET_USER:
                send_message("I'm available! 😊")

            last_message_id = message["id"]

        time.sleep(1)  # Check for new messages every 1 seconds

# Start the bot
auto_reply()
