from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

API_KEYS = {
    "anthropic_claude": os.getenv("ANTHROPIC_CLAUDE_API_KEY"),
    "google_gemini": os.getenv("GOOGLE_GEMINI_API_KEY"),
    "llama_3": os.getenv("LLAMA_3_API_KEY")
}

SYSTEM_PROMPT = """
You are an intelligent assistant. Your tasks include:
1. Answering questions accurately.
2. Using tools to fetch additional information when necessary.
3. Remembering user preferences and previous interactions.
4. Using chains to process input data and generate responses.
5. Retrieving relevant information using RAG.

Supported LLMs: Anthropic Claude 3, Google's Gemini, Llama 3.
"""

CHAT_HISTORY_FILE = os.getenv("CHAT_HISTORY_FILE")  # Path to the JSON file for chat history
PDF_PATH = os.getenv("PDF_PATH")  # Path to the PDF file
