import click
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger

setup_logger()

@click.command()
def main():
    try:
        print("\n🚀 Binance Futures Trading Bot\n")

        # 🔹 User Inputs (Interactive)
        symbol = click.prompt("Enter Symbol", default="BTCUSDT")

        side = click.prompt(
            "Enter Side (BUY/SELL)",
            type=click.Choice(["BUY", "SELL"], case_sensitive=False)
        ).upper()

        order_type = click.prompt(
            "Enter Order Type (MARKET/LIMIT/STOP)",
            type=click.Choice(["MARKET", "LIMIT", "STOP"], case_sensitive=False)
        ).upper()

        quantity = click.prompt("Enter Quantity", type=float)

        price = None
        if order_type in ["LIMIT", "STOP"]:
            price = click.prompt("Enter Price", type=float)

        # 🔹 Validation
        validate_order(symbol, side, order_type, quantity, price)

        client = get_client()

        # 🔹 Order Summary
        print("\n📌 Order Request Summary")
        print("------------------------")
        print(f"Symbol       : {symbol}")
        print(f"Side         : {side}")
        print(f"Order Type   : {order_type}")
        print(f"Quantity     : {quantity}")
        if price:
            print(f"Price        : {price}")

        # 🔹 Place Order
        order = place_order(client, symbol, side, order_type, quantity, price)

        # 🔹 Response
        print("\n📊 Order Response")
        print("------------------------")
        print(f"Order ID     : {order.get('orderId')}")
        print(f"Status       : {order.get('status')}")
        print(f"Executed Qty : {order.get('executedQty')}")
        print(f"Avg Price    : {order.get('avgPrice')}")

        print("\n✅ Order placed successfully\n")

    except Exception as e:
        print("\n❌ Error placing order")
        print(f"Reason: {str(e)}\n")


if __name__ == "__main__":
    main()