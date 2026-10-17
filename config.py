import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPERATOR_GROUP_ID = int(os.getenv("OPERATOR_GROUP_ID", 0))
ADMIN_IDS = [int(x.strip()) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip()]

# Throttling / Anti-spam
RATE_LIMIT_SECONDS = float(os.getenv("RATE_LIMIT_SECONDS", 2.0))

# AI / OpenAI / Gemini
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://generativelanguage.googleapis.com/v1beta/openai/")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gemini-1.5-flash")

# Database
DB_URL = os.getenv("DB_URL", "sqlite+aiosqlite:///./bot_database.db")

# Google Sheets Configuration
GOOGLE_SHEETS_URL = os.getenv("GOOGLE_SHEETS_URL", "")
GOOGLE_SPREADSHEET_ID = os.getenv("GOOGLE_SPREADSHEET_ID", GOOGLE_SHEETS_URL)
CREDENTIALS_FILE = os.getenv("CREDENTIALS_FILE", "credentials.json")
GOOGLE_CREDENTIALS_JSON = os.getenv("GOOGLE_CREDENTIALS_JSON", "")