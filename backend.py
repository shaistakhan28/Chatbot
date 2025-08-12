import cohere
import os
from dotenv import load_dotenv

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def get_text_output(history, user_message):
  
    cohere_history = []
    for msg in history:
        if msg["role"] == "USER":
            cohere_history.append({"role": "USER", "message": msg["message"]})
        else:
            cohere_history.append({"role": "CHATBOT", "message": msg["message"]})

    response = co.chat(
        model="command-r-plus",
        chat_history=cohere_history,
        message=user_message
    )

    return response.text

