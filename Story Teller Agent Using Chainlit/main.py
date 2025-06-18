import os
from dotenv import load_dotenv
import google.generativeai as genai
import chainlit as cl

# Load API key from .env
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=gemini_api_key)

# Load Gemini model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Chat start message
@cl.on_chat_start
async def Greeting():
    await cl.Message(
        content="👋 Hello! I'm a Story Teller Agent. How can I help you today?"
    ).send()

# Handle user messages
@cl.on_message
async def user_chat(message: cl.Message):
    prompt = f"Write a short story in Roman Urdu about: {message.content}"
    
    # Gemini response
    response = model.generate_content(prompt)

    # Send response to user
    await cl.Message(content=response.text).send()
