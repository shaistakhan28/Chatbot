import cohere
import os
from dotenv import load_dotenv,dotenv_values
load_dotenv()
co=cohere.Client(os.getenv("Cohere_API_KEY"))

def get_text_output(history,input_text):
    
    messages = history + [{"role": "USER", "message": input_text}]
    output=co.chat(
    model="command-r-plus",
    message=input_text
)
    return output.text
    
