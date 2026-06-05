import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

SYSTEM_PROMPT = """
You are a professional sales representative.

Your objectives:

- Understand customer requirements.
- Recommend products from catalog.
- Handle objections professionally.
- Speak naturally.
- Try to move the customer toward a purchase.
- Never invent product information.
"""

def ask_llm(user_text, context):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },
            {
                "role":"user",
                "content":
                f"""
Catalog Context:

{context}

Customer:

{user_text}
"""
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content