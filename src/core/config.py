"""
Lab 11 — Configuration & API Key Setup
"""
import os


def setup_api_key():
    """Load Google API key from environment or prompt."""
    from dotenv import load_dotenv
    
    # Load from .env file first
    load_dotenv()
    
    # Check for Google API key, fallback to OPENAI_API_KEY if available
    if "GOOGLE_API_KEY" not in os.environ:
        if "OPENAI_API_KEY" in os.environ:
            print("⚠ GOOGLE_API_KEY not found in .env")
            print("Note: This project requires Google API Key for Gemini models.")
            print("Get one free at: https://ai.google.dev/")
            api_key_input = input("Enter Google API Key (or 'skip' to use demo mode): ").strip()
            if api_key_input and api_key_input.lower() != 'skip':
                os.environ["GOOGLE_API_KEY"] = api_key_input
            else:
                print("⚠ Skipping Google API key setup - some features will be unavailable")
                return
        else:
            os.environ["GOOGLE_API_KEY"] = input("Enter Google API Key: ")
    
    print("✓ API key loaded (Google Gemini)")
    print(f"✓ Using model: gemini-2.0-flash")


# Allowed banking topics (used by topic_filter)
ALLOWED_TOPICS = [
    "banking", "account", "transaction", "transfer",
    "loan", "interest", "savings", "credit",
    "deposit", "withdrawal", "balance", "payment",
    "tai khoan", "giao dich", "tiet kiem", "lai suat",
    "chuyen tien", "the tin dung", "so du", "vay",
    "ngan hang", "atm",
]

# Blocked topics (immediate reject)
BLOCKED_TOPICS = [
    "hack", "exploit", "weapon", "drug", "illegal",
    "violence", "gambling", "bomb", "kill", "steal",
]
