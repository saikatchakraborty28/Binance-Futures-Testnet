

"""
Trading Bot Package
Handles Binance Futures Testnet trading operations
"""

from .client import get_client
from .order import place_order

__all__ = ["get_client", "place_order"]
__version__ = "1.0.0"