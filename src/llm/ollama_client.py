import os
from dotenv import load_dotenv
from llama_index.llms.ollama import Ollama
from llama_index.core import Settings

class OllamaClient:
    def __init__(self):
        load_dotenv()

        self.base_url = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
        self.model_name = os.getenv('MODEL_NAME', 'mistral:latest')

        self.llm = Ollama(
            model=self.model_name,
            base_url=self.base_url,
            temperature=0.7,
            request_timeout=60.0)
        
        # Configure global settings
        Settings.llm = self.llm