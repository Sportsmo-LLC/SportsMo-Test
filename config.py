from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
INVALID_PASSWORD = os.getenv("INVALID_PASSWORD")
