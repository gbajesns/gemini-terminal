from google import genai

import os

from dotenv import load_dotenv

load_dotenv()

api=os.getenv("API_KEY")

client = genai.Client(api_key=api)

while True:
	
	question = input("You: ")

	if question.lower() == "exit":
		break

	response = client.models.generate_content(model="gemini-3.6-flash", contents=question)

	print("Gemini:", response.text)
