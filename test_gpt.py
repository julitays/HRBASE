import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Ты helpful ассистент"},
        {"role": "user", "content": "Скажи коротко: работает ли мой ключ?"}
    ]
)

print(response.choices[0].message.content)
