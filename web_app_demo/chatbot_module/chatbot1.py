#!C:\Program Files\Python310\python.exe
print("content-type: text/html\n\n" )

import sys
import cgi

sys.path.append("C:\\Users\\tyree\\AppData\\Roaming\\Python\\Python310\\site-packages")

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# insantiating the chatbot
chatbot2 = ChatBot("DButler2", read_only=True)

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "Agent",
    "You're welcome.",
    "enjoy"
]
trainer = ListTrainer(chatbot2, show_training_progress=False)
trainer.train(conversation)

form=cgi.FieldStorage()
user_speech=form.getvalue("message_py")

bot_response = chatbot2.get_response(user_speech)

print(str(bot_response))
