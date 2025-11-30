import os
import json
from openai import OpenAI
from dotenv import load_dotenv

from backend.core.qdrant_client import get_qdrant_client
from backend.skills.translator import translate_to_urdu

# 1. Imports & Setup
load_dotenv()
client = OpenAI()
COLLECTION_NAME = "AIDD-BOOK"

# 2. Define Tool Functions
def search_textbook(query: str) -> str:
    """Searches the AIDD-BOOK Qdrant collection for relevant information."""
    qdrant_client = get_qdrant_client()

    search_result = qdrant_client.query(collection_name=COLLECTION_NAME, query_text=query, limit=3)

    # Formatted string logic
    context = ""
    for hit in search_result:
        # Note: With FastEmbed query(), the text is often in hit.document or hit.metadata['text']
        # Let's handle both cases to be safe
        doc_text = getattr(hit, "document", None) or hit.payload.get("text", "")
        context += f"---\n{doc_text}\n"

    return context

def translate_content(text: str) -> str:
    """Translates the given technical text into Urdu, keeping technical terms in English where appropriate."""
    return translate_to_urdu(text)

# 3. Define Tool Schemas
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_textbook",
            "description": "Searches the AIDD-BOOK for relevant information based on a query.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query for the textbook."
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "translate_content",
            "description": "Translates the provided technical text into Urdu, preserving technical terms.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The technical text to translate into Urdu."
                    }
                },
                "required": ["text"]
            }
        }
    }
]

# 4. Implement the Agent Class (`RoboticsProfessor`)
class RoboticsProfessor:
    def __init__(self):
        self.system_prompt = "You are an enthusiastic Robotics Professor. Use the 'search_textbook' tool to answer questions based strictly on the provided book content. If the user asks for Urdu translation, use the 'translate_content' tool."

    def chat(self, user_message: str, history: list) -> str:
        messages = history + [{"role": "user", "content": user_message}]

        response = client.chat.completions.create(
            model="gpt-4o-mini", # Or "gpt-4o"
            messages=[{"role": "system", "content": self.system_prompt}] + messages,
            tools=tools,
            tool_choice="auto"
        )

        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls

        if tool_calls:
            messages.append(response_message) # Extend conversation with assistant's reply

            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                if function_name == "search_textbook":
                    tool_output = search_textbook(query=function_args.get("query"))
                elif function_name == "translate_content":
                    tool_output = translate_content(text=function_args.get("text"))
                else:
                    tool_output = f"Error: Unknown tool {function_name}"

                messages.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": tool_output,
                })

            # Second API call to get the final response from the model
            second_response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": self.system_prompt}] + messages
            )
            return second_response.choices[0].message.content
        else:
            return response_message.content

# 5. Testing
if __name__ == "__main__":
    # For local testing, ensure OPENAI_API_KEY is set in your environment variables
    # or loaded from a .env file (for Qdrant client and Gemini skill as well).
    from dotenv import load_dotenv
    load_dotenv('../.env')

    professor_agent = RoboticsProfessor()
    initial_history = []

    print("\n--- Test 1: RAG Query ---")
    rag_query = "What is the difference between ROS 2 Topics and Services?"
    rag_response = professor_agent.chat(rag_query, initial_history)
    print(f"User: {rag_query}")
    print(f"Professor: {rag_response}")

    print("\n--- Test 2: Translation Query ---")
    translation_query = "Translate 'Hello, welcome to the Robotics course' to Urdu."
    translation_response = professor_agent.chat(translation_query, initial_history)
    print(f"User: {translation_query}")
    print(f"Professor: {translation_response}")

