# Trading Bot – Binance Futures Testnet

## Setup

1. Clone repo
2. Install dependencies:
   pip install -r requirements.txt

3. Create .env file:
   API_KEY=your_key
   API_SECRET=your_secret
   BASE_URL=https://testnet.binancefuture.com

## Usage

### Market Order
python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.01

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.01 --price 60000

## Features
- Market & Limit Orders
- CLI Input Validation
- Logging to file
- Error Handling

## Assumptions
- Only USDT pairs supported
- Testnet environment only