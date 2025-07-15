# refresh_logic.py

import os
import requests==2.31.0

def refresh_tokens_once():
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    refresh_token = os.getenv("REFRESH_TOKEN")

    url = "https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer"
    auth = (client_id, client_secret)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }

    response = requests.post(url, auth=auth, data=data)

    if response.status_code == 200:
        tokens = response.json()
        print("✅ Access token actualizado:", tokens["access_token"])
        print("🔁 Nuevo refresh token:", tokens["refresh_token"])
        # Aquí podrías guardar los tokens donde necesites
    else:
        print("❌ Error al refrescar token:", response.status_code, response.text)
