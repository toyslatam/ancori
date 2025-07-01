# refresh_worker.py

import time
import os
from main import refresh_tokens_once  # ← usa esta, no refresh_tokens

if __name__ == "__main__":
    print("🔄 Worker de tokens iniciado...")
    refresh_tokens_once()  # Esta ejecuta una sola vez el refresco
