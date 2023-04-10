import openai
from dotenv import load_dotenv
import os
from src.assistantVocal import AssistantVocal

class ChatGPT:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        self.model = model
        self.api_key = api_key
        openai.api_key = self.api_key
        self.messages = [{"role": "system", "content": "You are a helpful assistant."}]

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def get_response(self, user_message):
        self.add_message("user", user_message)
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )
        assistant_message = response.choices[0].message['content']
        self.add_message("assistant", assistant_message)
        return assistant_message

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("CHATGPT_API_KEY")
    chat_gpt = ChatGPT(api_key)

    pascal = AssistantVocal()

    user_message = pascal.ecouter_commande_vocale()
    response = chat_gpt.get_response(user_message)
    print(response)
    pascal.executer_commande_vocale(response)




