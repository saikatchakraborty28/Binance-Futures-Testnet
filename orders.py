import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        elif order_type == "STOP":   # 👈 ADD HERE
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP_MARKET",
                stopPrice=price,
                quantity=quantity
            )

        else:
            raise ValueError("Unsupported order type")

        logging.info(f"Order Success: {order}")
        return order

    except Exception as e:
        logging.error(f"Order Failed: {str(e)}")
        raise