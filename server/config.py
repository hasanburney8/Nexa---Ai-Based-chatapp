from dotenv import load_dotenv  # Loads environment variables from a .env file
from pydantic_settings import BaseSettings  # Base class for settings validation

# Load environment variables from a .env file
load_dotenv()

class Settings(BaseSettings):
    # API keys for external services (should be stored securely in a .env file)
    TAVILY_API_KEY: str = ""
    GEMINI_API_KEY: str = ""
