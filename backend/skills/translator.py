import os
import google.generativeai as genai

def translate_to_urdu(text: str) -> str:
    try:
        genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
        model = genai.GenerativeModel("gemini-2.5-flash")
        prompt = f"Translate the following technical text into Urdu. Keep technical terms (like ROS, Node, API) in English where appropriate: {text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error during translation: {e}")
        return text

if __name__ == "__main__":
    # For local testing, ensure GOOGLE_API_KEY is set in your environment variables
    # or loaded from a .env file.
    from dotenv import load_dotenv
    load_dotenv('../.env')

    test_text = "Hello, welcome to the Robotics course"
    translated_text = translate_to_urdu(test_text)
    print(f"Original: {test_text}")
    print(f"Translated: {translated_text}")
