from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

client = Client(
    os.getenv("API_KEY"),
    os.getenv("API_SECRET")
)

# 👇 Correct futures testnet endpoint
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

try:
    # ✅ This confirms API + SECRET are valid
    account_info = client.futures_account()

    print("✅ API KEY & SECRET ARE CORRECT")
    print("Balance:", account_info.get("totalWalletBalance"))

except Exception as e:
    print("❌ API ERROR:", str(e))