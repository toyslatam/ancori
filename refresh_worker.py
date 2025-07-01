# refresh_worker.py

import time
import os
from main import refresh_tokens  # Importa tu función desde main.py

if __name__ == "__main__":
    print("🔄 Worker de tokens iniciado...")
    refresh_tokens()  # Esto corre en loop (cada 55 min)
