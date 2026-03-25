from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

def conexaoGemini(pergunta):
    try:
        client = genai.Client(api_key=os.getenv("API_KEY_GEMINI"))
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=pergunta
        )
        return response.text
    except Exception as e:
        print("Error: ", e)
        return False