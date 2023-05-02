from dotenv import load_dotenv
load_dotenv()

import openai
import os

openai.api_key = os.environ.get("API_KEY")

def makeRequest(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

