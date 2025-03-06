# test.py

print("started")

# Import required libraries
from langchain_groq import ChatGroq  # This is for interacting with Groq LLaMA
import os  # To read environment variables
from dotenv import load_dotenv  # To load variables from .env file

# Load variables from .env
load_dotenv()

# Fetch the API key from environment variables
api_key = os.getenv("GROQ_API_KEY")
print(api_key)
# Check if the key was loaded properly
if not api_key:
    print("Error: GROQ_API_KEY is not set. Make sure your .env file is correct.")
else:
    # Initialize the ChatGroq object with your key
    llm = ChatGroq(temperature=0, groq_api_key=api_key, model_name="llama3-8b-8192")

    try:
        # Send a test message to see if it works
        response = llm.invoke("Say hello, this is a test message to check if the API key works.")
        print("API Key is valid! Response:")
        print(response.content)
    except Exception as e:
        print(f"API Key test failed: {e}")
