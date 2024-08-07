# utils/api_keys.py
from config.config.py import Config

def get_api_key(service_name):
    if service_name == 'gemma':
        return Config.GEMMA_API_KEY
    elif service_name == 'claude':
        return Config.CLAUDE_API_KEY
    elif service_name == 'llama':
        return Config.LLAMA_API_KEY
    else:
        raise ValueError("Unsupported service name")
