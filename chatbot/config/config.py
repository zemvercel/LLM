# config/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMMA_API_KEY = os.getenv('GEMMA_API_KEY')
    CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY')
    LLAMA_API_KEY = os.getenv('LLAMA_API_KEY')
